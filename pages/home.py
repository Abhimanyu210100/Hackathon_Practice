from datetime import date

import streamlit as st

from backend.data import get_all_clients
from frontend.styles import ACTIVE_STAGES, CSS, STAGE_META, STAGE_ORDER, badge, metric_tile

st.markdown(CSS, unsafe_allow_html=True)

# ── Greeting ─────────────────────────────────────────────────────────────────
user_name = st.session_state.get("user_name", "there")
today = date.today().strftime("%A, %B %-d %Y")

st.markdown(
    f'<div style="margin-bottom:4px">'
    f'<span style="font-size:1.7rem;font-weight:800;color:#1E293B">'
    f'Welcome back, {user_name} 👋</span>'
    f'</div>'
    f'<div style="color:#94A3B8;font-size:0.9rem;margin-bottom:28px">{today}</div>',
    unsafe_allow_html=True,
)

# ── Compute stats ─────────────────────────────────────────────────────────────
clients = get_all_clients()
active = [c for c in clients if c.deal_stage in ACTIVE_STAGES]
at_risk = [c for c in clients if c.deal_stage == "At Risk"]
pipeline_value = sum(c.deal_value for c in active)
overdue = [c for c in active if c.last_contact_days > 7]
in_negotiation = [c for c in clients if c.deal_stage == "Negotiation"]

# Priority score: higher = more urgent
def priority_score(c):
    score = 0
    if c.deal_stage == "At Risk":       score += 100
    if c.deal_stage == "Negotiation":   score += 50
    if c.last_contact_days > 21:        score += 40
    elif c.last_contact_days > 14:      score += 25
    elif c.last_contact_days > 7:       score += 10
    if c.deal_value > 150_000:          score += 20
    elif c.deal_value > 80_000:         score += 10
    return score

top_priority = sorted(active, key=priority_score, reverse=True)[:4]

# ── KPI row ──────────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">Pipeline Overview</div>', unsafe_allow_html=True)

k1, k2, k3, k4 = st.columns(4)
k1.markdown(metric_tile("Active Pipeline", f"${pipeline_value:,.0f}"), unsafe_allow_html=True)
k2.markdown(metric_tile("Active Deals", str(len(active))), unsafe_allow_html=True)
k3.markdown(
    metric_tile("Need Follow-Up", str(len(overdue)),
                value_color="#B45309" if overdue else "#065F46"),
    unsafe_allow_html=True,
)
k4.markdown(
    metric_tile("At Risk", str(len(at_risk)),
                value_color="#B91C1C" if at_risk else "#065F46"),
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# ── Stage breakdown + Today's focus (side by side) ───────────────────────────
col_stage, col_focus = st.columns([1, 1.4])

with col_stage:
    st.markdown('<div class="section-heading">Pipeline by Stage</div>', unsafe_allow_html=True)

    for stage in STAGE_ORDER:
        stage_clients = [c for c in clients if c.deal_stage == stage]
        if not stage_clients:
            continue
        total_val = sum(c.deal_value for c in stage_clients)
        m = STAGE_META.get(stage, {"bg": "#F1F5F9", "text": "#64748B", "icon": "·"})
        st.markdown(
            f'<div style="display:flex;align-items:center;justify-content:space-between;'
            f'padding:10px 14px;background:{m["bg"]};border-radius:8px;margin-bottom:6px;">'
            f'<div style="display:flex;align-items:center;gap:10px;">'
            f'<span style="font-size:1rem">{m["icon"]}</span>'
            f'<span style="font-weight:600;color:{m["text"]};font-size:0.88rem">{stage}</span>'
            f'</div>'
            f'<div style="text-align:right;">'
            f'<span style="font-size:0.75rem;color:#64748B">{len(stage_clients)} deal{"s" if len(stage_clients)!=1 else ""}</span>'
            f'<span style="margin-left:10px;font-weight:700;color:#1E293B;font-size:0.88rem">'
            f'${total_val:,.0f}</span>'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

with col_focus:
    st.markdown('<div class="section-heading">Today\'s Focus</div>', unsafe_allow_html=True)

    for client in top_priority:
        days_color = (
            "#B91C1C" if client.last_contact_days > 14 else
            "#B45309" if client.last_contact_days > 7 else
            "#065F46"
        )
        st.markdown(
            f'<div class="card" style="padding:14px 18px;margin-bottom:8px;">'
            f'<div style="display:flex;justify-content:space-between;align-items:center;">'
            f'<div>'
            f'<div style="font-weight:700;color:#1E293B;font-size:0.92rem">{client.name}</div>'
            f'<div style="color:#64748B;font-size:0.78rem">{client.company}</div>'
            f'</div>'
            f'<div style="text-align:right;">'
            f'{badge(client.deal_stage)}'
            f'<div style="font-size:0.75rem;color:{days_color};margin-top:4px;font-weight:600">'
            f'{client.last_contact_days}d since contact</div>'
            f'</div>'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

st.markdown("<hr>", unsafe_allow_html=True)

# ── Follow-up alerts ─────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">Follow-Up Required</div>', unsafe_allow_html=True)

if not overdue:
    st.markdown(
        '<div class="card card-green" style="text-align:center;padding:20px;">'
        '<span style="color:#065F46;font-weight:600">✓ All clients contacted within the last 7 days</span>'
        '</div>',
        unsafe_allow_html=True,
    )
else:
    overdue_sorted = sorted(overdue, key=lambda c: c.last_contact_days, reverse=True)
    cols = st.columns(min(len(overdue_sorted), 3))
    for i, client in enumerate(overdue_sorted):
        col = cols[i % 3]
        urgency_bg   = "#FFF5F5" if client.last_contact_days > 14 else "#FFFBEB"
        urgency_border = "#FECACA" if client.last_contact_days > 14 else "#FDE68A"
        urgency_text = "#B91C1C" if client.last_contact_days > 14 else "#92400E"

        col.markdown(
            f'<div style="background:{urgency_bg};border:1px solid {urgency_border};'
            f'border-radius:10px;padding:14px 16px;margin-bottom:8px;">'
            f'<div style="font-weight:700;color:#1E293B;font-size:0.88rem">{client.name}</div>'
            f'<div style="color:#64748B;font-size:0.78rem;margin:2px 0 8px">{client.company}</div>'
            f'{badge(client.deal_stage)}'
            f'<div style="margin-top:8px;font-size:0.8rem;font-weight:700;color:{urgency_text}">'
            f'⏱ {client.last_contact_days} days without contact</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

# ── Sidebar logout ────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("---")
    st.markdown(
        f'<div style="font-size:0.8rem;color:#94A3B8;padding:4px 0">'
        f'Logged in as <strong style="color:#475569">{user_name}</strong></div>',
        unsafe_allow_html=True,
    )
    if st.button("Log out", type="secondary", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
