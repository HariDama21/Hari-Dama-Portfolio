import streamlit as st
import time
import base64

st.title("Hello Streamlit")
st.header("header")
st.subheader("subheader")
st.text("i love streamlit")
st.text("""**i love streamlit
""")
st.markdown(""" # H1 tag
## H2 tag
### H3 tag 
:moon:<br>
:sunglasses:     
            
""",True)
st.balloons()

def home():
    
    # Page configs (tab title, favicon)
    st.set_page_config(
        with open("PY3/dp.png", "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()
    )

 social_icons_data = {
        # Platform: [URL, Icon]
        "Kaggle": ["https://www.kaggle.com/edomingo", "https://www.kaggle.com/static/images/site-logo.svg"],
        "LinkedIn": ["https://www.linkedin.com/in/e-domingo", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/enricd", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
        "Twitter": ["https://twitter.com/mad_enrico", "https://cdn-icons-png.flaticon.com/512/733/733579.png"],
        "YouTube": ["https://www.youtube.com/@enricd", "https://cdn-icons-png.flaticon.com/512/1384/1384060.png"],
        "Medium": ["https://medium.com/@enricdomingo", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Medium_logo_Monogram.svg/1200px-Medium_logo_Monogram.svg.png"]


with st.empty():
    for seconds in range(10):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("✔️ 10 seconds over!")


