import streamlit as st

from backend.data import get_all_clients, get_client_by_id
from core.recommendations import stream_recommendation

# ── Palette ──────────────────────────────────────────────────────────────────
STAGE_META = {
    "Prospecting":   {"icon": "○", "bg": "#DBEAFE", "text": "#1D4ED8"},
    "Qualification": {"icon": "◐", "bg": "#EDE9FE", "text": "#6D28D9"},
    "Proposal":      {"icon": "◑", "bg": "#FEF3C7", "text": "#B45309"},
    "Negotiation":   {"icon": "◕", "bg": "#FFEDD5", "text": "#C2410C"},
    "Closed Won":    {"icon": "●", "bg": "#D1FAE5", "text": "#065F46"},
    "At Risk":       {"icon": "!", "bg": "#FEE2E2", "text": "#B91C1C"},
}

CSS = """
<style>
/* ── Global ── */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #FFFFFF;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background-color: #F1F5F9;
    border-right: 1px solid #E2E8F0;
}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #1E293B;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

/* ── Sidebar client buttons ── */
[data-testid="stSidebar"] .stButton > button {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    color: #334155;
    font-size: 0.85rem;
    padding: 10px 12px;
    text-align: left;
    transition: all 0.15s ease;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background-color: #EFF6FF;
    border-color: #93C5FD;
    color: #1D4ED8;
}
[data-testid="stSidebar"] .stButton > button[kind="primary"] {
    background-color: #EFF6FF;
    border-color: #2563EB;
    color: #1D4ED8;
    font-weight: 600;
}

/* ── Cards ── */
.card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 12px;
}
.card-blue {
    background: #F0F7FF;
    border-color: #BFDBFE;
}
.card-grey {
    background: #F8FAFC;
    border-color: #E2E8F0;
}

/* ── Stage badge ── */
.stage-badge {
    display: inline-block;
    border-radius: 20px;
    padding: 4px 12px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.03em;
}

/* ── Metric tiles ── */
.metric-tile {
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
    padding: 14px 18px;
    text-align: center;
}
.metric-tile .label {
    font-size: 0.72rem;
    font-weight: 600;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 4px;
}
.metric-tile .value {
    font-size: 1.15rem;
    font-weight: 700;
    color: #1E293B;
}

/* ── Section headings ── */
.section-heading {
    font-size: 0.72rem;
    font-weight: 700;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 8px;
}

/* ── Pain point pills ── */
.pain-pill {
    display: inline-block;
    background: #F1F5F9;
    border: 1px solid #CBD5E1;
    border-radius: 6px;
    padding: 4px 10px;
    font-size: 0.82rem;
    color: #334155;
    margin: 3px 3px 3px 0;
}

/* ── Divider ── */
hr {
    border: none;
    border-top: 1px solid #E2E8F0;
    margin: 20px 0;
}

/* ── Primary button ── */
.stButton > button[kind="primary"] {
    background-color: #2563EB;
    border: none;
    border-radius: 8px;
    color: #FFFFFF;
    font-weight: 600;
    padding: 10px 20px;
    transition: background-color 0.15s ease;
}
.stButton > button[kind="primary"]:hover {
    background-color: #1D4ED8;
}

/* ── Secondary button ── */
.stButton > button[kind="secondary"] {
    background-color: #FFFFFF;
    border: 1px solid #CBD5E1;
    border-radius: 8px;
    color: #475569;
    font-weight: 500;
}
.stButton > button[kind="secondary"]:hover {
    border-color: #94A3B8;
    color: #1E293B;
}

/* ── AI output box ── */
.ai-box {
    background: #F0F7FF;
    border: 1px solid #BFDBFE;
    border-left: 4px solid #2563EB;
    border-radius: 10px;
    padding: 20px 24px;
    color: #1E293B;
    line-height: 1.65;
}

/* ── Page title ── */
h1 {
    color: #1E293B !important;
    font-weight: 800 !important;
}
</style>
"""


def _badge(stage: str) -> str:
    m = STAGE_META.get(stage, {"icon": "·", "bg": "#F1F5F9", "text": "#64748B"})
    return (
        f'<span class="stage-badge" '
        f'style="background:{m["bg"]};color:{m["text"]}">'
        f'{m["icon"]}  {stage}</span>'
    )


def _metric(label: str, value: str) -> str:
    return (
        f'<div class="metric-tile">'
        f'<div class="label">{label}</div>'
        f'<div class="value">{value}</div>'
        f'</div>'
    )


def render_app() -> None:
    st.set_page_config(
        page_title="Sales AI Assistant",
        page_icon="💼",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.markdown(CSS, unsafe_allow_html=True)

    clients = get_all_clients()

    # ── Sidebar ──────────────────────────────────────────────────────────────
    with st.sidebar:
        st.markdown("### 💼 Clients")

        # Stage filter
        all_stages = sorted({c.deal_stage for c in clients}, key=lambda s: [
            "Prospecting", "Qualification", "Proposal",
            "Negotiation", "At Risk", "Closed Won"
        ].index(s) if s in ["Prospecting", "Qualification", "Proposal",
                             "Negotiation", "At Risk", "Closed Won"] else 99)
        stage_filter = st.selectbox(
            "Filter by stage",
            ["All stages"] + all_stages,
            label_visibility="collapsed",
        )

        st.markdown("---")

        visible = clients if stage_filter == "All stages" else [
            c for c in clients if c.deal_stage == stage_filter
        ]

        for client in visible:
            m = STAGE_META.get(client.deal_stage, {"icon": "·"})
            label = f"{m['icon']} **{client.name}**  \n{client.company}"
            is_selected = st.session_state.get("selected_client_id") == client.id
            if st.button(
                label,
                key=f"btn_{client.id}",
                use_container_width=True,
                type="primary" if is_selected else "secondary",
            ):
                if not is_selected:
                    st.session_state.selected_client_id = client.id
                    st.session_state.pop("recommendation", None)
                st.rerun()

    # ── Main ─────────────────────────────────────────────────────────────────
    selected_id = st.session_state.get("selected_client_id")

    if not selected_id:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            '<div class="card card-grey" style="text-align:center;padding:48px;">'
            '<span style="font-size:2rem">👈</span><br><br>'
            '<span style="color:#64748B;font-size:1rem">'
            'Select a client from the sidebar to get started.'
            '</span></div>',
            unsafe_allow_html=True,
        )
        return

    client = get_client_by_id(selected_id)
    if not client:
        st.error("Client not found.")
        return

    # ── Client header card ────────────────────────────────────────────────────
    st.markdown(
        f'<div class="card">'
        f'<div style="display:flex;justify-content:space-between;align-items:flex-start;">'
        f'<div>'
        f'<div style="font-size:1.5rem;font-weight:800;color:#1E293B">{client.name}</div>'
        f'<div style="color:#64748B;margin:4px 0 10px">'
        f'{client.role} · <strong>{client.company}</strong> · {client.industry}'
        f'</div>'
        f'<div style="font-size:0.83rem;color:#94A3B8">📧 {client.email}</div>'
        f'</div>'
        f'<div>{_badge(client.deal_stage)}</div>'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

    # ── Metric row ────────────────────────────────────────────────────────────
    urgency_color = "#B91C1C" if client.last_contact_days > 14 else (
        "#B45309" if client.last_contact_days > 7 else "#065F46"
    )
    m1, m2, m3 = st.columns(3)
    m1.markdown(_metric("Deal Value", f"${client.deal_value:,}"), unsafe_allow_html=True)
    m2.markdown(_metric("Deal Stage", client.deal_stage), unsafe_allow_html=True)
    m3.markdown(
        f'<div class="metric-tile">'
        f'<div class="label">Last Contact</div>'
        f'<div class="value" style="color:{urgency_color}">'
        f'{client.last_contact_days}d ago</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Details ───────────────────────────────────────────────────────────────
    col_left, col_right = st.columns(2)

    with col_left:
        pills = "".join(f'<span class="pain-pill">{p}</span>' for p in client.pain_points)
        st.markdown(
            f'<div class="card card-grey">'
            f'<div class="section-heading">Pain Points</div>'
            f'{pills}'
            f'</div>',
            unsafe_allow_html=True,
        )

    with col_right:
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

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── AI Recommendation ─────────────────────────────────────────────────────
    st.markdown(
        '<div style="font-size:1.1rem;font-weight:700;color:#1E293B;margin-bottom:12px">'
        '🤖 AI Recommendation</div>',
        unsafe_allow_html=True,
    )

    if "recommendation" not in st.session_state:
        if st.button("✨ Generate Recommendation", type="primary"):
            try:
                recommendation = st.write_stream(stream_recommendation(client))
                st.session_state.recommendation = recommendation
                st.rerun()
            except Exception as e:
                st.error(f"Failed to generate recommendation: {e}")
    else:
        st.markdown(
            f'<div class="ai-box">{st.session_state.recommendation}</div>',
            unsafe_allow_html=True,
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔄 Regenerate", type="secondary"):
            del st.session_state.recommendation
            st.rerun()
