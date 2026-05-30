import streamlit as st

st.set_page_config(
    page_title="Sales AI Assistant",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

if not st.session_state.get("logged_in"):
    from frontend.auth import render_login
    render_login()
else:
    pg = st.navigation(
        [
            st.Page("pages/home.py",    title="Home",    icon="🏠"),
            st.Page("pages/clients.py", title="Clients", icon="👥"),
        ],
        position="sidebar",
    )
    pg.run()
