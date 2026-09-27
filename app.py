import streamlit as st

from auth.ui import show_auth_page, logout


# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Risk Analytics",
    page_icon="📊",
    layout="wide"
)


# -----------------------------------
# INITIALIZE SESSION STATE
# -----------------------------------

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "guest_mode" not in st.session_state:
    st.session_state.guest_mode = False

if "user" not in st.session_state:
    st.session_state.user = None


# -----------------------------------
# APPLICATION
# -----------------------------------

def show_application():

    st.title("Risk Analytics Platform")

    if st.session_state.authenticated:

        user = st.session_state.user

        if user:
            st.success(
                f"Logged in as {user.email}"
            )

        with st.sidebar:

            st.write("### Account")

            if st.button(
                "Logout",
                use_container_width=True
            ):
                logout()

    elif st.session_state.guest_mode:

        st.info(
            "You are using Risk Analytics as a Guest."
        )

        with st.sidebar:

            st.write("### Guest Mode")

            if st.button(
                "Exit Guest Mode",
                use_container_width=True
            ):

                st.session_state.guest_mode = False

                st.rerun()

    st.divider()

    st.header("Dashboard")

    st.write(
        "Your Risk Analytics dashboard will appear here."
    )


# -----------------------------------
# ACCESS CONTROL
# -----------------------------------

if (
    not st.session_state.authenticated
    and not st.session_state.guest_mode
):

    show_auth_page()

else:

    show_application()