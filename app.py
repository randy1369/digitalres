from pathlib import Path
import requests
from streamlit_lottie import st_lottie
import streamlit as st
from PIL import Image 

# Path Settings

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "ROX.pdf"



# General settings

PAGE_TITLE = "Digital Resume"
PAGE_ICON = "🧩"
NAME = "Rocks"
DESCRIPTION = """ 

A self-taught developer based in Hyderabad, India.

I am passionate about writing code and developing web applications to solve real-life challenges and have a natural curiosity to explore all aspects of technology. 🧑‍💻

My interests include DSA, Scripting, Web Dev, Machine Learning, AI, Blockchain, Cryptocurrency.

I believe that having a diverse range of interests and experiences helps me bring a unique perspective to my work.

    """
EMAIL = "johantheunknown@gmail.com"
SOCIAL_MEDIA = {
    "Youtube" : "https://youtube.com",
    "LinkedIn": "https://linkedin.com",
    "GitHub" : "https://github.com/randy1369?tab=repositories",
    "Twitter" : "https://twitter.com",
}

PROJECTS = {
    " Crypto Dashboard - Real-time Cryptocurrency Data Analysis": "https://cryptopricetracker-009.streamlit.app/",
    " Portfolio Website - Developed using Django, Html, CSS": "https://rox009.pythonanywhere.com/",
    " Blog - Built Using Djanog, Bootstrap5, with CRUD functionality and responsive Design": "https://rox006.pythonanywhere.com/",
    " GithubScraper - Built Using Python, BeautifulSoup, Streamlit": "https://top-repo-scraper.streamlit.app/",
    " Terminal Portfolio Site - Developed using Js, html, css" : "https://randy1369.github.io/rTerminal/",
}

#-------------------------------------------------------------------------------------------------------------------

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/56de7755-4643-410f-8f9d-c6c0193df878/6pHVCORtTV.json")


# --- LOAD CSS, PDF  ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()


# --- HERO SECTION ---

st.subheader("Hi, I am Rocks :wave:")
st.title("Python Developer")

with st.container():
    left_col, right_col = st.columns(2)
    with left_col:
        st.write(DESCRIPTION)
        left_download, right_contact = st.columns(2)
        with left_download:
            st.download_button(
                label=" 📄 Download Resume",
                data=PDFbyte,
                file_name=resume_file.name,
                mime="application/octet-stream",
            )
        with right_contact:
            st.write("📫", EMAIL)

    with right_col:
        st_lottie(lottie_coding, height=300, key="coding")


# --- SOCIAL LINKS ---
with st.container():
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

# --- EDUCATION ---
with st.container():
    st.write("---")
    st.subheader("Education")
    education_data = [
        {"Course": "B. Tech", "College/School": "Hindustan Institute Of Technology And Sciences", "% / CGPA": "8.5 CGPA"},
        {"Course": "Class XII", "College/School": "Narayana Junior College", "% / CGPA": "95%"},
        {"Course": "Class X", "College/School": "Narayana E.M High School", "% / CGPA": "9.3 CGPA"}
    ]
    st.table(education_data)



# --- SKILLS ---
# --- SKILLS ---
with st.container():
    st.write("---")
    st.subheader("Technical Skills")
    st.write(
        """
        - 👩‍💻 **Programming Languages:** Python, JavaScript

        - 📊 **Web Development:** Django, Flask, HTML, CSS, Bootstrap
        - 🔍 **Data Manipulation:** Beautiful Soup, Pandas
        - 📚 **Version Control:** Git, Bitbucket, GitHub
        - 🗄️ **Databases:** PostgreSQL, MongoDB, MySQL
        - ☁️ **Cloud Services:** AWS, Azure
        - 🚀 **Deployment and Virtualization:** Docker, Heroku
        - 🐧 **Operating Systems:** Linux, Windows
        """
    )



# --- Projects & Accomplishments ---
with st.container():
    st.write('\n')
    st.write("---")
    st.subheader("Projects & Accomplishments")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")


