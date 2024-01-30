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
    lottie_anime_json1 = load_lottie_url(lottie_animation_1)
    st_lottie(lottie_anime_json1,  width=650, height=650, key="initial")
    
    with col2:
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

    st_lottie(lottie_anime_json2,  speed=1, width=00, height=550, key="hello")

    
    st.header("",divider='rainbow')
    ##-------------------------------------------------------------------------------------PAGE 1 END--------------------------------------------------------------
if selected=="💼 Experience":
    def load_lottie_url(url: str):
       r = requests.get(url)
       if r.status_code != 200:
          return None
       return r.json()

    lottie_animation_1 = "https://lottie.host/9d0f401b-36e7-46ac-8127-9a4fd947d8c6/aB0aohwYCm.json"

    lottie_anime_json = load_lottie_url(lottie_animation_1)

    st_lottie(lottie_anime_json, speed=1, width=00, height=550, key="initial")
##---------------------------------------------------------------------------------------------------------------------------------------------
    selected=option_menu(
        menu_title=None,
        options=["DevX Community", "Smartinternz", "DDUGKY Audisankara", "Reliance JIO Telecommunication", "East Indian Pvt.Lmtd"],
        default_index=0,
        orientation="horizontal",
        styles={
                "container": {"padding": "0!important", "background-color": "#BBBB"},
                "icon": {"color": "orange", "font-size": "21px"},
                "nav-link": {
                    "font-size": "21px",
                    "text-align": "center",
                    "margin": "0px",
                    "--hover-color": "#bfbf",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
##------------------------------------------------------------------------------------------------------------------------------------------------------
    if selected=="DevX Community":
        st.header("Founder -  June 2023 To Present")
        st.header("",divider='rainbow')
        st.subheader("✭ A student-led community has been formed to encourage peer creativity and skill development.")
        st.subheader("✭ This effort allows aspirants to learn from one another, cooperate on projects, and develop their abilities in a safe setting.") 
        st.subheader("✭ The community is a gathering place for students to study, create, and invent.")
        st.subheader("✭ The community's specific goals include giving students the opportunity to learn new skills, stimulating innovation, creativity, establishing a collaborative atmosphere, and assisting them in developing the abilities they will need for their future employment.")
        st.subheader("✭ The community is committed to upskilling and innovation, creating an environment in which students may grow and create.")

        st.header("",divider='rainbow')

        st.image('pro_devx.jpeg')
    
        st.subheader("✭ Works Involved in")
        st.subheader("🔸 Community Building")
        st.subheader("🔹 Experts & Mentors Collaborations")
        st.subheader("🔸 Poster Designing")
        st.subheader("🔹 Hosting Sessions & Webinars")
        st.subheader("🔸 Social-Media Handling")
        st.subheader("🔹 Content Writing")
        st.subheader("🔸 Technical Support")
    
        col1, col2, col3 = st.columns(3)
        orientation = "center"
        with col1:
            st.link_button("Linkedin - DevX", "https://www.linkedin.com/company/devxcommunity/")
        with col2:
            st.empty()
        with col3:
            st.link_button("Instagram - DevX", "https://www.instagram.com/devx_grow_together?igsh=eThxeGV4ZGR5OWdy")
        def load_lottie_url(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
        lottie_animation_2 = "https://lottie.host/e9f8c073-ec63-4c11-8bb5-5cb1b156f97d/kwpWmONPuI.json"
        lottie_anime_json2 = load_lottie_url(lottie_animation_2)
        st_lottie(lottie_anime_json2, speed=1, width=00, height=550, key="initial3")
##------------------------------------------------------------------------------------------------------------------------------------------------------
    if selected=="Smartinternz":
        st.header("Salesforce Administration Intern -  May 2023 To July 2023")
        st.header("",divider='rainbow')
        st.subheader("✭ Learned Salesforce principles including user administration, data management, process automation, reporting, and dashboards.")
        st.subheader("✭ Covered topics like Salesforce security and system integrations.") 
        st.subheader("✭ User management involved creating and managing users, granting roles and permissions, and managing custom objects and fields.")
        st.subheader("✭ Process automation included building and configuring workflows and rules for corporate operations.")
        st.subheader("✭ Reporting and dashboards were developed to track and analyze critical KPIs. Salesforce security focused on setting up settings to protect data and prevent unauthorized access.")
        st.subheader("✭ Learned about system integrations, including email marketing platforms and CRM systems.")
        st.subheader("✭ Grateful for the opportunity to learn from experienced mentors at SmartInternz and eager to apply new skills in future Salesforce administration roles, aiming to streamline operations and improve customer interactions.")

        st.header("",divider='rainbow')

    
        st.subheader("✭ Works Involved in")
        st.subheader("🔸 Configure Ste-up menu, Process builder, Workflow Rules and Page Layouts")
        st.subheader("🔹 Data Modelling, Security and Access Controll")
        st.subheader("🔸 Creating Reports and Dashboards")
        st.subheader("🔹 Creating Triggers")
        st.subheader("🔹 Creating Web Pages in Salesforce Cloud")

    
    
        tab1, tab2, tab3 = st.tabs(["Image-1", "Image-2", "Image-3"])
        with tab1:
            st.header("Skills Gaind & Trigger Flows")
            st.image("pro_sm1.png", width=None)
        with tab2:
            st.header("Dashboards")
            st.image("pro_sm2.png", width=None)
        with tab3:
            st.header("Static Web App in Salesforce Cloud")
            st.image("pro_sm3.png", width=None)
    
        st.link_button("DevX Salesforce", "https://brave-badger-60tpul-dev-ed.trailblaze.my.site.com/portfolio/s/")

        def load_lottie_url(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
        lottie_animation_2 = "https://lottie.host/0fd5bc3a-d261-484a-ae53-a42cd479f5c8/uSW245AQwE.json"
        lottie_anime_json2 = load_lottie_url(lottie_animation_2)
        st_lottie(lottie_anime_json2, speed=1, width=00, height=550, key="initial4")


##_-----------------------------------------------------------------------------------------------------------------------------------------------------
    if selected=="DDUGKY Audisankara":
        st.header("MIS & Receptionist -  March 2021 To February 2022")
        st.header("",divider='rainbow')
        st.subheader("✭ Aishwarya Vignan Educational Society (Audisankara Group of Institutions) is also used to run skill india projectstanding on Deen Dayal Upadhyay Grameen Kaushalya Yojana.")
        st.subheader("✭ Use to handle sites like Kaushalbharat.gov.in, which contain total informationCollect, organize, and store data for various organizational activities.") 
        st.subheader("✭ The role involves data management, technology and MIS enhancement, receptionist duties, administrative support, security and access control, and multitasking. ")
        st.subheader("✭ It involves ensuring data accuracy, maintaining consistency, and staying updated on emerging technologies.")
        st.subheader("✭ The role also involves handling office supplies and maintaining a tidy reception area.")

        st.header("",divider='rainbow')

        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Training Introduction", "Training Center-1", "Training Center-2", "Training Center-3", "Superior", "Notice Board", "E-Learning"])
        with tab1:
            video_file = open('vid.mp4', 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)
        with tab2:
            st.header("Training Class Romms")
            st.image("cen1.jpg", width=850)
        with tab3:
            st.header("MIS & Counseling Cabins")
            st.image("cen2.jpg", width=850)
        with tab4:
            st.header("Training Center")
            st.image("cen3.jpg", width=500)
        with tab5:
            st.header("Dr.A.Immanuel")
            st.image("sir.png", width=500)
        with tab6:
            st.header("Things Distributed to Individuals During Training")
            st.image("cen4.jpg", width=850)
        with tab7:
            st.header("E-Learning Through Installed LMS")
            st.image("cen5.jpg", width=850)
        
        def load_lottie_url(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
        lottie_animation_9 = "https://lottie.host/7aef3025-24cb-4eac-aba1-74b78fb051d7/L2dyt1HKzn.json"
        lottie_anime_json9 = load_lottie_url(lottie_animation_9)
        st_lottie(lottie_anime_json9, speed=1, width=00, height=350, key="initial9")

        col1, col2, col3 = st.columns(3)
        orientation = "center"
        with col1:
            st.image("DDU1.jpg", width=None)
        with col2:
            st.image("DDU2.jpg", width=None)
        with col3:
            st.image("DDU3.jpg", width=None)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.empty()
        with col2:
            st.markdown("***Our Mobilization Camp's in various Mandal's of Tiruvallur District, Tamilnadu***")
        with col3:
            st.empty()

        st.header("",divider='rainbow')
##------------------------------------------------------------------------------------------------------------------------------------------------------
    if selected=="Reliance JIO Telecommunication":
        st.header("Sales Executive -  November 2019 To September 2020")
        st.header("",divider='rainbow')
        st.subheader("✭ Promote & sell product using solid arguments to existing and prospective customers")
        st.subheader("✭ Develop & maintain positive business and customer relationships") 
        st.subheader("✭ The role involves acquiring new customers for Jio telecom services, conducting sales presentations, meeting sales targets, developing strategies, building strong customer relationships, addressing customer inquiries, conducting market research, staying updated on industry trends, collaborating with internal teams, and working closely with marketing and technical teams.")
        st.subheader("✭ The role also involves participating in training sessions to enhance product knowledge and sales skills and staying informed about Jio product and service updates.")

        
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.empty()
        with col2:
            st.image('jio.png', width=700)
        with col3:
            st.empty()

        col1, col2, col3 = st.columns(3)
        with col1:
            st.empty()
        with col2:
            st.markdown("***JIO Centre Manager expresses gratitude for the second-most sales in the Tirupathi region.***")
        with col3:
            st.empty()
        
        st.header("",divider='rainbow')


##------------------------------------------------------------------------------------------------------------------------------------------------------
    if selected=="East Indian Pvt.Lmtd":
        st.header("PCB Testing -  September 2018 To February 2019")
        st.header("",divider='rainbow')
        st.subheader("✭ Integrated PCB manufacturing involves designing, prototyping, testing, and mass-producing printed circuit boards. The process includes assembling electronic components and inspecting them for quality assurance.")
        st.subheader("✭ Integrated PCB (printed circuit board) production entails a number of steps:") 
        st.subheader("✭ When designing the circuit, printing it, etching the board, drilling holes, plating, applying the solder mask, silk screen printing, placing the components, soldering, and testing.")

        def load_lottie_url(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
        lottie_animation_8= "https://lottie.host/d1668828-c19d-4d71-bed3-ac58de623f48/ZqP3wWnLyA.json"
        lottie_anime_json8 = load_lottie_url(lottie_animation_8)
        st_lottie(lottie_anime_json8, speed=1, width=00, height=550, key="initial6")
        
        st.header("",divider='rainbow')
##----------------------------------------------------------PAGG 2 END ----------------------------------------------------------------------------------

if selected=="👥 DevX Community":
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

    def load_lottie_url(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_animation_7 = "https://lottie.host/72c5da03-052f-48ab-bb97-b6fa6a656629/WUSORYFsZt.json"
    lottie_anime_json7 = load_lottie_url(lottie_animation_7)
    st_lottie(lottie_anime_json7, speed=1, width=00, height=595, key="initial")
        
    st.image("6.png", width=None)

    st.header("",divider='rainbow')

##--------------------------------------------PAGE 3 END-----------------------------------------------------------------

if selected=="🤳🏻 Photography":
    st.subheader(":rainbow[Welcome to the world of XAPN Prospectives] 📸")
    st.header("",divider='rainbow')
##---------------------------------------------------------------------------------------------------------------------------------------------
    col1, col2 = st.columns(2)
    with col1:
        st.image("5pro.jpg",width=825)
    with col2:
        st.subheader("👋🏻:grey[Hello, are you curious? Why am I displaying the phone, which is expanding its lens?]")
        st.subheader(":grey[✭ If so, don't worry about it. I'm here to explain.]")

        st.header("*:rainbow[i am Hari Dama, an passionate photographer. who's interested in Landscapes, Stargazing, Low Light & Macro photography realated areas.]*")
        st.subheader("✭ Everything began with the pandemic of COVID, and everyone stayed at home due to curfews.")
        st.subheader("✭ I have plenty of time to experiment at the moment. I discovered some photography-related stuff, such as how to edit images.")
        st.subheader("✭ I thought this might help me take better photos. Then it went on for a long time, and I learned how to photograph from various angles and framings.")
        st.subheader("✭ So, without hesitation, I continued to master the core concepts of photography, such as the exposure triangle, which includes shutter speed, aperture, and ISO.")
        st.subheader("✭ Various camera modes include auto, programme auto, shutter priority, aperture priority, and, ultimately, to manual mode.*")
        st.subheader("✭ At that point, I discovered that every smartphone includes a manual camera mode.")
        st.subheader("✭ I was surprised to learn that. How is this possible? Here begins the exploratory journey.")

        st.subheader(":red[Note :]If you truly want to succeed on our trip, never consider other people's opinions.")
        st.subheader("✭ Everyone compliments your job positively. But, are they willing to pay for it? Obviously, no.")
        st.subheader("✭ There's a saying about opinions: opinions are like a**holes; everyone had one (no offense here 😀).")
        st.subheader(":rainbow[All images were taken with the Realme Pro]😎🤘🏻.")

    st.header("",divider='rainbow')
##---------------------------------------------------------------------------------------------------------------------------------------------
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("idol1.jpg",width=None) 
    with col2:
        st.image("idol2.jpg",width=None)
    with col3:
        st.image("idol3.jpg",width=None)
##---------------------------------------------------------------------------------------------------------------------------------------------
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("ls1.jpg",width=None) 
    with col2:
        st.image("ls2.jpeg",width=None)
    with col3:
        st.image("ls3.jpg",width=None)
##---------------------------------------------------------------------------------------------------------------------------------------------
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("pwl1.jpg",width=None) 
    with col2:
        st.image("pwl2.jpg",width=None)
    with col3:
        st.image("pwl3.jpg",width=None)
##---------------------------------------------------------------------------------------------------------------------------------------------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("st1.jpg",width=None) 
    with col2:
        st.image("st2.jpg",width=None)
        st.image("st5.jpg",width=None)
    with col3:
        st.image("st3.jpg",width=None)
        st.image("st4.jpeg",width=None)

    def load_lottie_url(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_animation_6 = "https://lottie.host/464b9049-bc48-4404-b8da-5fdff2a3a1cf/rYW0dXLeKF.json"
    lottie_anime_json6 = load_lottie_url(lottie_animation_6)
    st_lottie(lottie_anime_json6, speed=1, width=00, height=550, key="initial")
##---------------------------------------------------------------------------------------------------------------------------------------------
    tab1, tab2, tab3, tab4 = st.tabs(["1️⃣", "2️⃣", "3️⃣", "4️⃣"])
    with tab1:
        st.image("pano1.jpg",width=None)        
    with tab2:
        st.image("pano2.jpeg", width=None)
    with tab3:
        st.image("pano3.jpg", width=None)
    with tab4:
        st.image("sky.jpeg",width=None)
##---------------------------------------------------------------------------------------------------------------------------------------------
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("mac1.jpeg",width=None) 
    with col2:
        st.image("mac2.jpg",width=None)
    with col3:
        st.image("mac3.jpeg",width=None)
##---------------------------------------------------------------------------------------------------------------------------------------------
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("mac4.jpg",width=None) 
    with col2:
        st.image("mac5.jpg",width=None)
    with col3:
        st.image("mac6.jpg",width=None)
##---------------------------------------------------------------------------------------------------------------------------------------------
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("sky1.jpg",width=None) 
    with col2:
        st.image("sky2.jpeg",width=None)
    with col3:
        st.image("sky3.jpg",width=None)
    
    st.header("",divider='rainbow')

##--------------------------------------------THE END-----------------------------------------------------------------


