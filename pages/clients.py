import streamlit as st

from backend.data import get_all_clients, get_client_by_id
from core.recommendations import stream_recommendation
from frontend.styles import CSS, STAGE_META, STAGE_ORDER, badge, metric_tile

st.markdown(CSS, unsafe_allow_html=True)

clients = get_all_clients()

# ── Sidebar: client list ──────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### Clients")

    stage_filter = st.selectbox(
        "Filter by stage",
        ["All stages"] + STAGE_ORDER,
        label_visibility="collapsed",
    )

    st.markdown("---")

    visible = (
        clients if stage_filter == "All stages"
        else [c for c in clients if c.deal_stage == stage_filter]
    )

    for client in visible:
        m = STAGE_META.get(client.deal_stage, {"icon": "·"})
        is_selected = st.session_state.get("selected_client_id") == client.id
        if st.button(
            f"{m['icon']} **{client.name}**  \n{client.company}",
            key=f"btn_{client.id}",
            use_container_width=True,
            type="primary" if is_selected else "secondary",
        ):
            if not is_selected:
                st.session_state.selected_client_id = client.id
                st.session_state.pop("recommendation", None)
            st.rerun()

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

# ── Main area ─────────────────────────────────────────────────────────────────
selected_id = st.session_state.get("selected_client_id")

if not selected_id:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        '<div class="card card-grey" style="text-align:center;padding:64px;">'
        '<span style="font-size:2.5rem">👈</span><br><br>'
        '<span style="color:#64748B;font-size:1rem">'
        'Select a client from the sidebar to view their profile.'
        '</span></div>',
        unsafe_allow_html=True,
    )
    st.stop()

client = get_client_by_id(selected_id)
if not client:
    st.error("Client not found.")
    st.stop()

# ── Client header card ────────────────────────────────────────────────────────
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
    f'<div>{badge(client.deal_stage)}</div>'
    f'</div>'
    f'</div>',
    unsafe_allow_html=True,
)

# ── Metric row ────────────────────────────────────────────────────────────────
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

# ── Details ───────────────────────────────────────────────────────────────────
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

# ── AI Recommendation ─────────────────────────────────────────────────────────
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
