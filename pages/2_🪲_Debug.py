import streamlit as st

path_to_logo = r"assets\images\the_witcher_3__wild_hunt_logo.jpg"
st.set_page_config(
        page_title="Witcher 3: Wild Hunt - Board Game", 
        layout="wide", 
        initial_sidebar_state="expanded",
        page_icon= path_to_logo
)

sidebar_logo = path_to_logo
main_body_logo = path_to_logo
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


