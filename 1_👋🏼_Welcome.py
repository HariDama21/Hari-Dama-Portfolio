import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

orientation="horizontal"
st.set_page_config(
    page_title="Hari Dama",
    page_icon="✨",
    layout="wide"
)

def main():
    st.title("My Portfolio")

selected=option_menu(
        menu_title=None,
        options=["✨ Home", "💼 Experience", "👥 DevX Community", "🤳🏻 Photography"],
        default_index=0,
        orientation="horizontal",
        styles={
                "container": {"padding": "0!important", "background-color": "#BBBB"},
                "icon": {"color": "orange", "font-size": "21px"},
                "nav-link": {
                    "font-size": "21px",
                    "text-align": "center",
                    "margin": "0px",
                    "--hover-color": "#0009",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )




if selected=="✨ Home":
    st.subheader("👋🏻:rainbow[Hola , I hope you're doing well. Welcome to my portfolio!]")
    st.header("",divider='rainbow')
    col1, col2 = st.columns(2)
    with col1:
        def load_lottie_url(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

    lottie_animation_1 = "https://lottie.host/9f38b8b5-3d51-4466-9e90-e57de7c47142/46DUUW0Z0Y.json"
    lottie_anime_json = load_lottie_url(lottie_animation_1)
    st_lottie(lottie_anime_json,  width=900, height=800, key="initial")
    
    with col12:
        st.image("dp.png", width=600)

    st.title("Hari Dama")

    st.subheader("𝙰𝚜𝚙𝚒𝚛𝚒𝚗𝚐 𝙲𝚕𝚘𝚞𝚍 𝙴𝚗𝚐𝚒𝚗𝚎𝚎𝚛 ✭ 𝙳𝚎𝚟𝚇 ✭ 𝟸𝚡 𝙾𝚁𝙰𝙲𝙻𝙴 ✭ 𝙻𝚒𝚗𝚔𝚎𝚍𝙸𝚗 𝙼𝚊𝚛𝚔𝚎𝚝𝚒𝚗𝚐𝙸𝚗𝚜𝚒𝚍𝚎𝚛 ✭ 𝚂𝚊𝚕𝚎𝚜𝚏𝚘𝚛𝚌𝚎𝙰𝚍𝚖𝚒𝚗𝚒𝚜𝚝𝚛𝚊𝚝𝚘𝚛 ✭ 𝙰𝙸 & 𝙼𝙻", divider='rainbow')

    col1, col2, col3 = st.columns(3)
    orientation = "center"
    with col1:
        st.image("ln.png", width=89)
        st.link_button("Linkedin", "https://www.linkedin.com/in/iamharidama/")
    with col2:
        st.image("gt.png", width=89)
        st.link_button("GitHub", "https://github.com/HariDama21")
    with col3:
        st.image("x.png", width=89)
        st.link_button("X", "https://x.com/h3devx?t=kQY6ukd7S25JqG9sRG_RRA&s=08")

    st.subheader("***👋🏻 Hi, my name is Hari***")

    st.subheader("*🎓 Soon to be grad with a Bachelor's of Technology in Artificial Intelligence (2024) and Completed Diploma in Electronics and Communication Engineering.*")

    st.subheader("*🌇 Andhra Pradesh Native, with a passion for creating Photographs and learning technology that will upskill my knowledge.*")

    st.subheader("*✨ Want to be a developer, where I can deploy new things based on my knowledge with team coordination.*")

    st.subheader("*💻 In my free time, you can find me learning and implementing new  things in the real world.*")

    st.subheader("*💪🏻 #Java_Programmer #Python.*")


    def load_lottie_url(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_animation_2 = "https://lottie.host/2b260cb0-6c43-45e3-a8bc-4c46f0bc34f2/J86tLnJF7z.json"

    lottie_anime_json2 = load_lottie_url(lottie_animation_2)

    st_lottie(lottie_anime_json2, key = "hello2", width=898)

    ##THE END
    st.header("",divider='rainbow')
