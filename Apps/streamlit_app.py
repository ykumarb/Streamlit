# --- Import required modules to create web app ---
import streamlit as st

# --- All Global variables go here ---
nav = None

# --- Function definitios go here --- 
# Function to setup the navigation in the web app.
# Without sections
def setup_streamlit_navigation_wo_section():
    global nav
    # --- Navigation Setup [ Without Sections ] ---
    nav = st.navigation(pages=[about_page, sales_dashboard_project_page, chatbot_project_page, contact_page])

# Function to setup the navigation in the web app.
# With sections
def setup_streamlit_navigation_section():
    global nav
    # --- Navigation Setup [ With Sections ] ---
    nav = st.navigation(
        {
            "Info": [about_page],
            "Projects": [sales_dashboard_project_page, chatbot_project_page],
            "Contact": [contact_page],
        }
    )

# --- Main application goes here --- 
# st.title("Hello Yupindra!!!")

# --- Page Setup ---
about_page = st.Page(
    page="views/about_me.py",
    title="About Me", 
    icon=":material/account_circle:",
    default=True,
)

sales_dashboard_project_page = st.Page(
    page="views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)

chatbot_project_page = st.Page(
    page="views/chatbot.py",
    title="Chatbot",
    icon=":material/smart_toy:",
)

contact_page = st.Page(
    page="views/contact.py",
    title="Contact Me",
    icon=":material/contacts_product:",
)

# Setup the navigation w/o section - Disabled
# setup_streamlit_navigation_wo_section()

# Setup the navigation with section
setup_streamlit_navigation_section()

# --- Shared on all the pages ---
st.logo("assets/neat.png")
st.sidebar.text("Made with 💓 by Yupindra ")

# --- Run the Navigation ---
nav.run()