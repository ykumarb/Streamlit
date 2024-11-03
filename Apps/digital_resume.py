from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile_image1.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Yupindra Kumar"
PAGE_ICON = ":wave:"
NAME = "Yupindra Kumar"
DESCRIPTION = """
Senior Software Engineer, assisting enterprises by developing drivers/fimrware for embedded systems.
"""
EMAIL = "yupindrakumarbalaji@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 4 years experience in embedded software domain
- ✔️ Strong hands-on experience and Knowledge in Linux Based Residential Gateways
- ✔️ Hands-on experience working with openWRT/RDKB based Mesh Solutions.
- ✔️ Worked on Qualcomm CSON Mesh solution for Telecom Client
- ✔️ Strong understanding in SDIO/PCIe Driver development
- ✔️ Proficiency in DMA programming and differnet Flow Control mechanism in Bus interface
- ✔️ Good understanding of ARM Cortex-M Architecture and bring-up of MCUs with Host Software Stack
- ✔️ Proficiency in embedded C Programming, Python, Bash scripting
- ✔️ Excellent team player and displaying a strong sense of initiative on tasks.

"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: embedded C, C++, Python, Bash, HTML, CSS, Javascript, C#
- 📊 Data Visulization: MS Excel, Matplotlib
- 📚 Frameworks: React, Node, Express JS
- 🗄️ Databases: MongoDB
- 🗄️ HW Architecture: ARM-CR4, ARM-M55, ARM-CM4, ARM-M7
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write('\n')
st.write("🚧", "**Senior Software Engineer | embedUR Systems**")
st.write("08/2020 - Present")
st.write(
    """
- ► Built Hardware Abstraction layer for Broadcom WLAN HND driver
- ► Built Wi-Fi driver and bug fixing on Broadcom Chipset
- ► Integrated Qualcomm CSON into non-Qualcomm platforms and developed several Wi-Fi features
- ► Integrated and brought-up threadx/freertos based system in different cores of a single combo chip.
- ► Worked on openWRT/RDK-B based Residential gateways.
- ► Several developmens in Pcie/Sdio based device drivers.
- ► Implemented M2M DMA mechanism b/w Host and Driver
"""
)

# --- JOB 2
st.write("🚧", "**Software Engineer | Tollun Technologies**")
st.write("08/2020 - Present")
st.write(
    """
- ► Used Python Django framework to create Web Application
- ► Used Python to create Chatbot for client
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")