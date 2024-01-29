import streamlit as st
from streamlit_gspread import GSheetsConnection

import pandas as pd

st.set_page_config(
    page_title="Let's Connect",
    page_icon="✉",
    layout="wide"
)

st.title(" Contact Form")
st.markdown("Dont be a stranger...! 👋")

conn = st.experimental_connection("gsheets", type=GSheetsConnection)

existing_data = conn.read(worksheet="Form", usecols=list(range(6)), ttl=5)

st.dataframe(existing_data)

import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def setup_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("your-credentials-file.json", scope)
    gc = gspread.authorize(credentials)
    sheet = gc.open("Your Google Sheet Title").sheet1
    return sheet

def main():
    st.title("Contact Form App")

    with st.form("Contact Form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")

        if submitted:
            if name and email and message:
                sheet = setup_google_sheets()
                sheet.append_row([name, email, message])
                st.success("Form submitted successfully!")
            else:
                st.warning("Please fill out all the fields.")

if __name__ == "__main__":
    main()
