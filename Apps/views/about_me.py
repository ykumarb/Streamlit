# --- Import required modules to create web app ---
import streamlit as st
from forms.contact import contact_form

# --- All Global variables go here ---
column_cnt=2

# --- Function definitios go here --- 
# To turn the code inside the function
# as a pop-up window decorate it
@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

# --- Main application goes here --- 
# st.title("About Me!")

# --- Hero Section ---
col1, col2 = st.columns(column_cnt, gap="small", vertical_alignment="center")
with col1:
    st.image("assets/profile_image1.png", width=230)
with col2:
    st.title("Yupindra Kumar", anchor=False)
    st.write(
        "Senior Software Engineer, assisting enterprises by developing drivers/fimrware for embedded systems."
    )
    if st.button("✉ Contact Me"):
        show_contact_form()


# --- Education Details ----
st.write("\n")
st.subheader("Education", anchor=False)
st.write(
    """
    - Bachelor of Engineering in Electronics and Communication
    - 🎓 2016 - 2020
    - 🏁 Chennai, India
    """
)

# --- Experience and Qualifications ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 4 years experience in embedded software domain
    - Strong hands-on experience and Knowledge in Linux Based Residential Gateways
    - Hands-on experience working with openWRT/RDKB based Mesh Solutions.
    - Worked on Qualcomm CSON Mesh solution for Telecom Client
    - Strong understanding in SDIO/PCIe Driver development
    - Proficiency in DMA programming and differnet Flow Control mechanism in Bus interface
    - Good understanding of ARM Cortex-M Architecture and bring-up of MCUs with Host Software Stack
    - Proficiency in embedded C Programming, Python, Bash scripting
    - Excellent team player and displaying a strong sense of initiative on tasks.
    """
)

# --- Skills ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: embedded C, C++, Python, Bash, HTML, CSS, Javascript
    - Frameworks: React, Node, Express JS
    - Databases: MongoDB
    - Data Visualization: MS Excel, Matplotlib
    - HW Architecture: ARM-CR4, ARM-M55, ARM-CM4, ARM-M7
    """
)

# --- Certifications ---
st.write("\n")
st.subheader("Certifications", anchor=False)
st.write(
    """
    - Certified Python Programmer
    """
)
