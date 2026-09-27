import streamlit as st

from auth.auth_service import sign_up, sign_in, sign_out


def show_auth_page():
    """
    Display the authentication screen.
    """

    st.title("Risk Analytics Platform")

    st.write(
        "Analyze portfolio performance, risk, diversification, "
        "and more."
    )

    st.divider()

    login_tab, signup_tab = st.tabs(
        ["Login", "Create Account"]
    )

    # -------------------------
    # LOGIN
    # -------------------------
    with login_tab:

        st.subheader("Login")

        email = st.text_input(
            "Email",
            key="login_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button(
            "Login",
            use_container_width=True
        ):

            if not email or not password:
                st.warning(
                    "Please enter your email and password."
                )

            else:
                response, error = sign_in(
                    email,
                    password
                )

                if error:

                    st.error(
                        f"Login failed: {error}"
                    )

                else:

                    st.session_state.authenticated = True
                    st.session_state.guest_mode = False
                    st.session_state.user = response.user

                    st.success(
                        "Login successful!"
                    )

                    st.rerun()

    # -------------------------
    # SIGN UP
    # -------------------------
    with signup_tab:

        st.subheader("Create Account")

        email = st.text_input(
            "Email",
            key="signup_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="signup_password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            key="signup_confirm_password"
        )

        if st.button(
            "Create Account",
            use_container_width=True
        ):

            if not email or not password:
                st.warning(
                    "Please enter your email and password."
                )

            elif password != confirm_password:
                st.error(
                    "Passwords do not match."
                )

            elif len(password) < 6:
                st.error(
                    "Password must be at least 6 characters."
                )

            else:

                response, error = sign_up(
                    email,
                    password
                )

                if error:

                    st.error(
                        f"Signup failed: {error}"
                    )

                else:

                    st.success(
                        "Account created successfully!"
                    )

                    st.info(
                        "Please check your email and "
                        "confirm your account before logging in."
                    )

    st.divider()

    # -------------------------
    # GUEST MODE
    # -------------------------

    st.subheader("Don't want to create an account?")

    if st.button(
        "Continue as Guest",
        use_container_width=True
    ):

        st.session_state.authenticated = False
        st.session_state.guest_mode = True
        st.session_state.user = None

        st.rerun()


def logout():

    success, error = sign_out()

    if success:

        st.session_state.authenticated = False
        st.session_state.guest_mode = False
        st.session_state.user = None

        st.rerun()

    else:

        st.error(
            f"Logout failed: {error}"
        )