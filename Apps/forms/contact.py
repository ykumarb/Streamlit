# --- Import required modules to create web app ---
import streamlit as st
import re
import requests

# --- All Global variables go here ---
WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZjMDYzMjA0MzY1MjZjNTUzYzUxMzMi_pc"

# --- Function definitios go here --- 


# --- Main application goes here --- 
# st.title("Contact me!")

# Function to validate email
def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

# Function to put form contents for contact
def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            st.success("Message successfully sent")
            if not WEBHOOK_URL:
                st.error(
                    "Email Service is not set up. Please try again later.", icon="📧"
                )
                st.stop()
            if not name:
                st.error("Please provide your name.", icon="👦")
                st.stop()

            if not email:
                st.error("Please provide your email address.", icon="✉")
                st.stop()

            if not is_valid_email(email):
                st.error("Please provide a valid email address.", icon="📧")
                st.stop()

            if not message:
                st.error("Please provide a message.", icon="💌")
                st.stop()

            # Prepare the data payload and send it to the specified webhook URL
            data = {"email": email, "name": name, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.success("Your message has been sent successfully! 🎉", icon="🚀")
            else:
                st.error("There was an error sending your message.", icon="😥")