import streamlit as st

st.set_page_config(
        page_title="Witcher 3: Wild Hunt - Board Game", 
        layout="wide", 
        initial_sidebar_state="expanded",
        page_icon= "the_witcher_3__wild_hunt_logo__original_sticker__by_kejo13_d7tjk8e-fullview.jpg"
)

sidebar_logo = "the_witcher_3__wild_hunt_logo__original_sticker__by_kejo13_d7tjk8e-fullview.jpg"
main_body_logo = "the_witcher_3__wild_hunt_logo__original_sticker__by_kejo13_d7tjk8e-fullview.jpg"
st.logo(sidebar_logo, size="large", icon_image=main_body_logo)

st.title("Logs")
st.write("This is a debug page with logs.")

if 'logs_list' in st.session_state:
        st.write(st.session_state.logs_list)
else:
        st.write(":red[No logs yet.]")