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

# st.write(st.session_state)

st.title("DEBUG")
st.header("This is a debug page to check :orange[session_state] contents.")
st.write(f"Whole app has been run :orange[{st.session_state.counter}] times within current session.") 

st.subheader("Contents of MOST_RECENTLY_CHOSEN_TOKEN:", divider = True)
if 'most_recently_chosen_token' in st.session_state:
        st.write(st.session_state.most_recently_chosen_token)
else:
        st.write(":red[No most_recently_chosen_token yet.]")
        
st.subheader("Contents of REMOVED_TRAIL_TOKENS_BAG:", divider = True)
# with st.expander("See detailed list:"):
if 'REMOVED_TRAIL_TOKENS_BAG' in st.session_state:
        st.write(st.session_state.REMOVED_TRAIL_TOKENS_BAG)
else:
        st.write(":red[No REMOVED_TRAIL_TOKENS_BAG yet.]")

st.subheader("Contents of REMOVED_WEAKNESS_TOKENS_BAG:", divider = True)
if 'REMOVED_WEAKNESS_TOKENS_BAG' in st.session_state:
        st.write(st.session_state.REMOVED_WEAKNESS_TOKENS_BAG)
else:
        st.write(":red[No REMOVED_WEAKNESS_TOKENS_BAG yet.]")

st.subheader("Contents of WEAKNESS_TOKENS_BAG:", divider = True)
if 'WEAKNESS_TOKENS_BAG' in st.session_state:
        st.write(st.session_state.WEAKNESS_TOKENS_BAG)
else:
        st.write(":red[No WEAKNESS_TOKENS_BAG yet.]")

st.subheader("Contents of TRAIL_TOKENS_BAG:", divider = True)
if 'TRAIL_TOKENS_BAG' in st.session_state:
        st.write(st.session_state.TRAIL_TOKENS_BAG)
else:
        st.write(":red[No TRAIL_TOKENS_BAG yet.]")


