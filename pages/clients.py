import streamlit as st

import re

from backend.data import get_all_clients, get_client_by_id
from core.recommendations import parse_recommendation, stream_recommendation
from frontend.styles import (
    ACTIVE_STAGES, ARCHIVED_STAGES, CSS, STAGE_META, badge, metric_tile,
)

TYPE_COLORS = {
    "Email":    ("#DBEAFE", "#1D4ED8"),
    "Call":     ("#D1FAE5", "#065F46"),
    "LinkedIn": ("#EDE9FE", "#6D28D9"),
    "Demo":     ("#FEF3C7", "#B45309"),
    "Meeting":  ("#E0E7FF", "#3730A3"),
    "Contract": ("#CCFBF1", "#0F766E"),
    "Internal": ("#F1F5F9", "#475569"),
    "Webinar":  ("#FEF9C3", "#854D0E"),
}


def _fmt_date(iso: str) -> str:
    from datetime import date
    d = date.fromisoformat(iso)
    return d.strftime("%b %-d, %Y")


def _render_interaction_history(client) -> None:
    history = client.interaction_history
    if not history:
        return
    with st.expander(f"Interaction History  ·  {len(history)} touchpoints", expanded=False):
        rows_html = []
        for entry in history:
            bg, fg = TYPE_COLORS.get(entry.type, ("#F1F5F9", "#475569"))
            badge = (
                f'<span style="display:inline-block;background:{bg};color:{fg};'
                f'border-radius:20px;padding:3px 10px;font-size:0.72rem;font-weight:700;'
                f'white-space:nowrap">{entry.type}</span>'
            )
            rows_html.append(
                f'<div style="display:flex;align-items:flex-start;gap:14px;'
                f'padding:10px 0;border-bottom:1px solid #F1F5F9">'
                f'<div style="min-width:82px;padding-top:1px">{badge}</div>'
                f'<div style="flex:1">'
                f'<div style="font-size:0.74rem;color:#94A3B8;margin-bottom:3px">{_fmt_date(entry.date)}</div>'
                f'<div style="font-size:0.87rem;color:#334155;line-height:1.5">{entry.summary}</div>'
                f'</div></div>'
            )
        # Remove bottom border on last row
        if rows_html:
            rows_html[-1] = rows_html[-1].replace("border-bottom:1px solid #F1F5F9", "border-bottom:none")
        st.markdown(
            f'<div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;'
            f'padding:4px 16px">{"".join(rows_html)}</div>',
            unsafe_allow_html=True,
        )


def _bullets_to_html(text: str) -> str:
    """Convert '- item' lines to an HTML list; wrap other lines in <p> tags."""
    lines = text.strip().splitlines()
    out, in_list = [], False
    for line in lines:
        s = line.strip()
        if s.startswith("- "):
            if not in_list:
                out.append('<ul style="margin:6px 0 6px 4px;padding-left:18px;">')
                in_list = True
            item = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", s[2:])
            out.append(f'<li style="margin:4px 0;color:#334155;line-height:1.55">{item}</li>')
        else:
            if in_list:
                out.append("</ul>")
                in_list = False
            if s:
                s = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", s)
                out.append(f'<p style="margin:5px 0;color:#334155;line-height:1.6">{s}</p>')
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def _render_recommendation(text: str) -> None:
    sections = parse_recommendation(text)

    # ── Situation Summary ─────────────────────────────────────────────────────
    situation = sections.get("situation", "")
    if situation:
        st.markdown(
            f'<div style="background:#EFF6FF;border:1px solid #BFDBFE;'
            f'border-left:4px solid #2563EB;border-radius:10px;padding:16px 20px;margin-bottom:14px">'
            f'<div class="section-heading" style="color:#2563EB;margin-bottom:10px">'
            f'📍 SITUATION SUMMARY</div>'
            f'{_bullets_to_html(situation)}</div>',
            unsafe_allow_html=True,
        )

    # ── Reasoning ─────────────────────────────────────────────────────────────
    reasoning = sections.get("reasoning", "")
    if reasoning:
        st.markdown(
            f'<div style="background:#F0FDF4;border:1px solid #BBF7D0;'
            f'border-left:4px solid #16A34A;border-radius:10px;padding:16px 20px;margin-bottom:14px">'
            f'<div class="section-heading" style="color:#16A34A;margin-bottom:10px">'
            f'🧠 REASONING</div>'
            f'{_bullets_to_html(reasoning)}</div>',
            unsafe_allow_html=True,
        )

    # ── Outreach ──────────────────────────────────────────────────────────────
    outreach = sections.get("outreach", "")
    if outreach:
        lines = outreach.splitlines()
        channel, subject, body_lines, past_divider = "", "", [], False
        for line in lines:
            lower = line.lower()
            if lower.startswith("channel:"):
                channel = line.split(":", 1)[1].strip()
            elif lower.startswith("subject:"):
                subject = line.split(":", 1)[1].strip()
            elif line.strip() == "---":
                past_divider = True
            else:
                body_lines.append(line)
        body = "\n".join(body_lines).strip()

        channel_colors = {
            "email":    ("#FEF3C7", "#B45309"),
            "linkedin": ("#DBEAFE", "#1D4ED8"),
            "phone":    ("#F3E8FF", "#7C3AED"),
        }
        ch_bg, ch_fg = channel_colors.get(channel.lower(), ("#F1F5F9", "#475569"))
        channel_badge = (
            f'<span style="background:{ch_bg};color:{ch_fg};border-radius:20px;'
            f'padding:3px 11px;font-size:0.75rem;font-weight:700;margin-left:8px">'
            f'{channel}</span>'
            if channel else ""
        )
        subject_html = (
            f'<div style="font-size:0.82rem;font-weight:600;color:#334155;margin:10px 0 4px">'
            f'Subject: {subject}</div>'
            if subject else ""
        )
        body_html = (
            f'<div style="background:#FFFBEB;border:1px solid #FDE68A;border-radius:8px;'
            f'padding:14px 16px;font-size:0.88rem;color:#1E293B;white-space:pre-wrap;'
            f'line-height:1.65;margin-top:10px">{body}</div>'
        )
        st.markdown(
            f'<div style="background:#FFF7ED;border:1px solid #FED7AA;'
            f'border-left:4px solid #EA580C;border-radius:10px;padding:16px 20px;margin-bottom:14px">'
            f'<div style="display:flex;align-items:center;margin-bottom:2px">'
            f'<div class="section-heading" style="color:#EA580C;margin-bottom:0">'
            f'✉️ OUTREACH</div>{channel_badge}</div>'
            f'{subject_html}{body_html}</div>',
            unsafe_allow_html=True,
        )

    if not sections:
        st.markdown(
            f'<div class="ai-box">{text}</div>',
            unsafe_allow_html=True,
        )


st.markdown(CSS, unsafe_allow_html=True)

# ── Sidebar: logout only ──────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("---")
    user_name = st.session_state.get("user_name", "")
    st.markdown(
        f'<div style="font-size:0.8rem;color:#94A3B8;padding:4px 0">'
        f'Logged in as <strong style="color:#475569">{user_name}</strong></div>',
        unsafe_allow_html=True,
    )
    if st.button("Log out", key="logout_clients", type="secondary", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

all_clients = get_all_clients()

# ── Detail view ───────────────────────────────────────────────────────────────
if st.session_state.get("selected_client_id"):
    client = get_client_by_id(st.session_state.selected_client_id)

    if not client:
        st.error("Client not found.")
        st.stop()

    if st.button("← Back to all clients", type="secondary"):
        del st.session_state["selected_client_id"]
        st.session_state.pop("recommendation", None)
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        f'<div class="card">'
        f'<div style="display:flex;justify-content:space-between;align-items:flex-start;">'
        f'<div>'
        f'<div style="font-size:1.5rem;font-weight:800;color:#1E293B">{client.name}</div>'
        f'<div style="color:#64748B;margin:4px 0 10px">'
        f'{client.role} · <strong>{client.company}</strong> · {client.industry}</div>'
        f'<div style="font-size:0.83rem;color:#94A3B8">📧 {client.email}</div>'
        f'</div>'
        f'<div>{badge(client.deal_stage)}</div>'
        f'</div></div>',
        unsafe_allow_html=True,
    )

    days_color = (
        "#B91C1C" if client.last_contact_days > 14 else
        "#B45309" if client.last_contact_days > 7 else
        "#065F46"
    )
    m1, m2, m3 = st.columns(3)
    m1.markdown(metric_tile("Deal Value", f"${client.deal_value:,}"), unsafe_allow_html=True)
    m2.markdown(metric_tile("Deal Stage", client.deal_stage), unsafe_allow_html=True)
    m3.markdown(
        metric_tile("Last Contact", f"{client.last_contact_days}d ago", value_color=days_color),
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col_l, col_r = st.columns(2)
    with col_l:
        pills = "".join(f'<span class="pain-pill">{p}</span>' for p in client.pain_points)
        st.markdown(
            f'<div class="card card-grey"><div class="section-heading">Pain Points</div>'
            f'{pills}</div>',
            unsafe_allow_html=True,
        )
    with col_r:
        st.markdown(
            f'<div class="card card-grey">'
            f'<div class="section-heading">Recent Activity</div>'
            f'<div style="font-size:0.88rem;color:#334155;margin-bottom:14px">'
            f'{client.recent_activity}</div>'
            f'<div class="section-heading">Notes</div>'
            f'<div style="font-size:0.88rem;color:#334155">{client.notes}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    _render_interaction_history(client)

    # Only show AI recommendation for active deals
    if client.deal_stage not in ARCHIVED_STAGES:
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size:1.1rem;font-weight:700;color:#1E293B;margin-bottom:12px">'
            '🤖 AI Recommendation</div>',
            unsafe_allow_html=True,
        )
        if "recommendation" not in st.session_state:
            if st.button("✨ Generate Recommendation", type="primary"):
                try:
                    rec = st.write_stream(stream_recommendation(client))
                    st.session_state.recommendation = rec
                    st.rerun()
                except Exception as e:
                    st.error(f"Failed to generate recommendation: {e}")
        else:
            _render_recommendation(st.session_state.recommendation)
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🔄 Regenerate", type="secondary"):
                del st.session_state.recommendation
                st.rerun()

    st.stop()

# ── Client list view ──────────────────────────────────────────────────────────
active_clients   = [c for c in all_clients if c.deal_stage in ACTIVE_STAGES]
archived_clients = [c for c in all_clients if c.deal_stage in ARCHIVED_STAGES]

tab_active, tab_archived = st.tabs([
    f"🟢 Active  ({len(active_clients)})",
    f"🗂  Archived  ({len(archived_clients)})",
])


def _render_client_list(clients, tab_key: str, filter_stages: list[str]) -> None:
    """Render filter controls + card grid for a given client list."""
    if not clients:
        st.markdown(
            '<div class="card card-grey" style="text-align:center;padding:48px;">'
            '<span style="color:#64748B">No clients in this section.</span></div>',
            unsafe_allow_html=True,
        )
        return

    # ── Controls ──────────────────────────────────────────────────────────────
    fc1, fc2, fc3 = st.columns([2, 1.6, 1])

    with fc1:
        selected_stages = st.multiselect(
            "Filter by stage",
            options=filter_stages,
            default=[],
            placeholder="All stages",
            key=f"stage_filter_{tab_key}",
        )

    with fc2:
        sort_by = st.selectbox(
            "Sort by",
            options=[
                "Days since contact ↓ (most overdue first)",
                "Days since contact ↑ (most recent first)",
                "Deal value ↓ (highest first)",
                "Deal value ↑ (lowest first)",
                "Name A–Z",
            ],
            key=f"sort_{tab_key}",
        )

    filtered = clients if not selected_stages else [
        c for c in clients if c.deal_stage in selected_stages
    ]

    with fc3:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="padding-top:6px;font-size:0.85rem;color:#64748B">'
            f'Showing <strong style="color:#1E293B">{len(filtered)}</strong> clients</div>',
            unsafe_allow_html=True,
        )

    sort_key_map = {
        "Days since contact ↓ (most overdue first)":  (lambda c: c.last_contact_days, True),
        "Days since contact ↑ (most recent first)":   (lambda c: c.last_contact_days, False),
        "Deal value ↓ (highest first)":               (lambda c: c.deal_value,        True),
        "Deal value ↑ (lowest first)":                (lambda c: c.deal_value,        False),
        "Name A–Z":                                   (lambda c: c.name.lower(),      False),
    }
    sort_fn, reverse = sort_key_map[sort_by]
    sorted_clients = sorted(filtered, key=sort_fn, reverse=reverse)

    if not sorted_clients:
        st.markdown(
            '<div class="card card-grey" style="text-align:center;padding:32px;margin-top:16px;">'
            '<span style="color:#64748B">No clients match the selected filters.</span></div>',
            unsafe_allow_html=True,
        )
        return

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Cards ─────────────────────────────────────────────────────────────────
    for i in range(0, len(sorted_clients), 2):
        col_a, col_b = st.columns(2)
        for col, client in zip([col_a, col_b], sorted_clients[i:i + 2]):
            days_color = (
                "#B91C1C" if client.last_contact_days > 14 else
                "#B45309" if client.last_contact_days > 7 else
                "#065F46"
            )
            # Muted card style for archived entries
            card_style = (
                'background:#F8FAFC;border:1px solid #E2E8F0;'
                if client.deal_stage in ARCHIVED_STAGES
                else ''
            )
            with col:
                st.markdown(
                    f'<div class="card" style="{card_style}margin-bottom:4px;">'
                    f'<div style="display:flex;justify-content:space-between;'
                    f'align-items:flex-start;margin-bottom:10px;">'
                    f'<div>'
                    f'<div style="font-weight:700;font-size:1rem;color:#1E293B">'
                    f'{client.name}</div>'
                    f'<div style="font-size:0.8rem;color:#64748B;margin-top:2px">'
                    f'{client.role} · {client.company}</div>'
                    f'</div>'
                    f'{badge(client.deal_stage)}'
                    f'</div>'
                    f'<div style="display:flex;justify-content:space-between;'
                    f'align-items:center;border-top:1px solid #F1F5F9;'
                    f'padding-top:10px;margin-top:4px;">'
                    f'<div>'
                    f'<div style="font-size:0.7rem;color:#94A3B8;font-weight:600;'
                    f'text-transform:uppercase;letter-spacing:.05em">Deal Value</div>'
                    f'<div style="font-size:0.95rem;font-weight:700;color:#1E293B">'
                    f'${client.deal_value:,}</div>'
                    f'</div>'
                    f'<div style="text-align:right;">'
                    f'<div style="font-size:0.7rem;color:#94A3B8;font-weight:600;'
                    f'text-transform:uppercase;letter-spacing:.05em">Last Contact</div>'
                    f'<div style="font-size:0.95rem;font-weight:700;color:{days_color}">'
                    f'{client.last_contact_days}d ago</div>'
                    f'</div>'
                    f'<div style="font-size:0.75rem;color:#64748B;font-style:italic">'
                    f'{client.industry}</div>'
                    f'</div>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
                if st.button(
                    "View profile →",
                    key=f"open_{tab_key}_{client.id}",
                    use_container_width=True,
                ):
                    st.session_state.selected_client_id = client.id
                    st.session_state.pop("recommendation", None)
                    st.rerun()


with tab_active:
    st.markdown("<br>", unsafe_allow_html=True)
    _render_client_list(active_clients, tab_key="active", filter_stages=ACTIVE_STAGES)

with tab_archived:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        '<div class="card card-grey" style="padding:12px 18px;margin-bottom:16px;">'
        '<span style="font-size:0.85rem;color:#64748B">'
        '🗂  Archived deals are read-only. '
        'AI recommendations are not available for closed deals.'
        '</span></div>',
        unsafe_allow_html=True,
    )
    _render_client_list(archived_clients, tab_key="archived", filter_stages=ARCHIVED_STAGES)
