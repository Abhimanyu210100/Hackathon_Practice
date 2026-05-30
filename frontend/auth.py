import streamlit as st

from frontend.styles import CSS

LOGIN_CSS = """
<style>
/* centre the login card on the page */
.login-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 80vh;
}
.login-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 48px 40px;
    width: 100%;
    max-width: 420px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.06);
    text-align: center;
}
.login-card .app-icon  { font-size: 2.8rem; margin-bottom: 8px; }
.login-card .app-title {
    font-size: 1.6rem;
    font-weight: 800;
    color: #1E293B;
    margin-bottom: 4px;
}
.login-card .app-sub {
    font-size: 0.9rem;
    color: #64748B;
    margin-bottom: 32px;
}
/* tighten the Streamlit input labels */
label { font-size: 0.83rem !important; color: #475569 !important; font-weight: 600 !important; }
</style>
"""


def render_login() -> None:
    st.markdown(CSS + LOGIN_CSS, unsafe_allow_html=True)

    _, col, _ = st.columns([1, 1.6, 1])

    with col:
        st.markdown(
            '<div class="login-card">'
            '<div class="app-icon">💼</div>'
            '<div class="app-title">Sales AI Assistant</div>'
            '<div class="app-sub">Your AI-powered B2B sales companion</div>'
            '</div>',
            unsafe_allow_html=True,
        )

        name = st.text_input("Your name", placeholder="e.g. Alex Johnson")
        st.text_input("Password", type="password", placeholder="Any password works")

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("Log in →", type="primary", use_container_width=True):
            if name.strip():
                st.session_state.logged_in = True
                st.session_state.user_name = name.strip()
                st.rerun()
            else:
                st.warning("Please enter your name to continue.")
