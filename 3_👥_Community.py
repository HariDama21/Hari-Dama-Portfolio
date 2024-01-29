import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Community Building",
    page_icon="🌟",
    layout="wide"
)
##--------------------------------------------------------------------------------------------------------------------------------------------
col1, col2 = st.columns(2)
with col1:
    def load_lottie_url(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

lottie_animation_1 = "https://lottie.host/f8e974a9-8b8d-4fce-889b-e66c1d25968b/09IdWFPSnQ.json"

lottie_anime_json = load_lottie_url(lottie_animation_1)

st_lottie(lottie_anime_json, key = "hello", width=1100)

with col2:
    st.image("devxl.png", width=600)
st.subheader(":rainbow[Let's Explore Our Community 'DevX' ]")

col1, col2 = st.columns(2)
with col1:
    st.link_button("Linkedin - DevX", "https://www.linkedin.com/company/devxcommunity/")
with col2:
    st.link_button("Instagram - DevX", "https://www.instagram.com/devx_grow_together?igsh=eThxeGV4ZGR5OWdy")

st.header("",divider='rainbow')
##---------------------------------------------------------------------------------------------------------------------------------------------
st.subheader("💭 I’ll explain all you need to know about DevX and why you should join us.")
st.image("1.png", width=None)
st.subheader("✭ Okay, here we go with the narration. It all started in our pre-final year of undergrad.")
st.subheader("✭ Myself, Hari Dama, and Mr. Anil Kumar Dagada are all fascinated by technology.")
st.subheader("✭ We went through some event tickets at ZOHO Chennai, which is organised by Google Developer Groups Cloud Chennai, one fine day. We were delighted to be attending Cloud Community Day 2023.")

st.image("2.png", width=None)

st.subheader("✭ The radical revolutionary ideas were born. We’ve met a lot of people in the tech field who are incredibly humble and simple.")
st.subheader("✭ The fantastic thing about this community is that the majority of them are students who are already studying and exploring numerous prospects in technology. That enlightened us and pushed us to create DevX.")
st.subheader("✭ We are extremely delighted by the opportunity to build relationships with such excellent people.")
st.header("***:rainbow[DevX is one of the greatest ideas we explored.]***")
st.header("***:rainbow[The goal of DevX is to bridge the gap between newbies and professionals in order for them to gain industry-relevant skills and build projects.]***")

st.image("3.png", width=None)

st.subheader("✭ We are unable to establish the Google Developer Student Club (GDSC) at our college.")
st.subheader("✭ GDSC is a programme that assists university students in their path towards mastering developer technologies.")
st.subheader("✭ Google-related technologies can be learned and collaborated on in GDSC’s.")
st.subheader("✭ However, in DevX, we have incorporated a wide range of technologies for you to explore and develop a phenomenal career.")

st.image("4.png", width=None)

st.subheader("✭ We teamed up with several industrial experts to mentor the newbies in the meantime.")
st.subheader("✭ The leads will guide you throughout the process of learning in your respective domain.")
st.subheader("✭ We also aimed to hold sessions on LinkedIn profile optimisation and advanced AI tools for increased productivity.")

st.header("***🌟:rainbow[“DevX is a family, not just a tech community.”]***")
st.header("***:rainbow[We help each other, learn, and grow together.]***")
st.header("***:rainbow[Whether you are a beginner or an expert, DevX has a place for you.]***")

st.image("5.png", width=None)

st.subheader("✭ We are grateful that DevX is not just a part of a tier-3 college.")
st.subheader("✭ Many students from IITs and MITs, as well as professionals from other IT professions, attended.")
st.subheader("✭ Human resource recruiters who are actively looking for talent are also members of DevX.")
st.subheader("✭ We’d like to thank Deepak Puram, who founded the We Are Developers community, for acting as a role model for us to launch our own tech community.")

st.header("***🌟:rainbow[We express our gratitude to GDG Cloud Chennai, GDG Chennai, TechBound, GDSC MBU, and KARE, as well as the mentors of DevX, for providing their valuable time to guide aspirants to their dream careers and to every individual who was involved in DevX’s success.]***")

st.image("6.png", width=None)

st.header("",divider='rainbow')

##--------------------------------------------THE END-----------------------------------------------------------------