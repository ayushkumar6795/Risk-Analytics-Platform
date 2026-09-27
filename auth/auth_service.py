from auth.supabase_client import supabase


def sign_up(email, password):
    try:
        response = supabase.auth.sign_up({
            "email": email,
            "password": password
        })

        return response, None

    except Exception as e:
        return None, str(e)


def sign_in(email, password):
    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        return response, None

    except Exception as e:
        return None, str(e)


def sign_out():
    try:
        supabase.auth.sign_out()
        return True, None

    except Exception as e:
        return False, str(e)


def get_current_user():
    try:
        response = supabase.auth.get_user()

        if response and response.user:
            return response.user

        return None

    except Exception:
        return None