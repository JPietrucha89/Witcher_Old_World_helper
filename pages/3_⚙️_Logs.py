import streamlit as st
import modules.tokens as tokens

path_to_logo = r"assets/images/the_witcher_3__wild_hunt_logo.jpg"

st.set_page_config(
        page_title="Witcher 3: Wild Hunt - Board Game", 
        layout="wide", 
        initial_sidebar_state="expanded",
        page_icon= path_to_logo
)

sidebar_logo = path_to_logo
main_body_logo = path_to_logo
st.logo(sidebar_logo, size="large", icon_image=main_body_logo)



st.title("Logs")
st.write("This is a debug page with logs.")

if 'logs_list' in st.session_state:
        st.write(st.session_state.logs_list)
else:
        st.write(":red[No logs yet.]")