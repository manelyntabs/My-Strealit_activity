import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# --- User Credentials (You can store this externally or load securely)
config = {
    'credentials': {
        'usernames': {
            'jsmith': {
                'name': 'John Smith',
                'password': stauth.Hasher(['123']).generate()[0]  # hashed password
            },
            'rdoe': {
                'name': 'Rebecca Doe',
                'password': stauth.Hasher(['abc']).generate()[0]
            }
        }
    },
    'cookie': {
        'name': 'my_app',
        'key': 'some_signature_key',  # Must be secure in production
        'expiry_days': 30
    },
    'preauthorized': {
        'emails': []
    }
}

# --- Authenticator setup
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# --- Login UI
name, authentication_status, username = authenticator.login("Login", "main")

# --- Post-login logic
if authentication_status:
    st.sidebar.success(f"Welcome {name}")
    authenticator.logout("Logout", "sidebar")

    st.title("Your Data App")
    st.write("Secure content goes here...")

elif authentication_status is False:
    st.error("Username/password is incorrect")
elif authentication_status is None:
    st.warning("Please enter your username and password")
