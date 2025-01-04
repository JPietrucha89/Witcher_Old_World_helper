import tokens
import random
import streamlit as st

global TRAIL_TOKENS_BAG
global WEAKNESS_TOKENS_BAG
global REMOVED_TRAIL_TOKENS_BAG
global REMOVED_WEAKNESS_TOKENS_BAG
global most_recently_chosen_token
global session_state

def page_config():
    st.set_page_config(
        page_title="Witcher 3: Wild Hunt - Board Game", 
        layout="wide", 
        initial_sidebar_state="expanded",
        page_icon= "the_witcher_3__wild_hunt_logo__original_sticker__by_kejo13_d7tjk8e-fullview.jpg"
    )

    sidebar_logo = "the_witcher_3__wild_hunt_logo__original_sticker__by_kejo13_d7tjk8e-fullview.jpg"
    main_body_logo = "the_witcher_3__wild_hunt_logo__original_sticker__by_kejo13_d7tjk8e-fullview.jpg"
    st.logo(sidebar_logo, size="large", icon_image=main_body_logo)

    with st.sidebar:
        st.image("the_witcher_3__wild_hunt_logo__original_sticker__by_kejo13_d7tjk8e-fullview.jpg")

        st.markdown(
        '<a href="mailto:elpietruch@gmail.com">Contact me!</a>',
        unsafe_allow_html=True
        )

def myFunc(e):
    return e.token_fullname

def get_color_for_token(token_name):
    if isinstance(token_name, str):
        pass
    else:
        token_name = token_name.token_fullname

    if 'FOREST' in token_name:
        return 'green'
    if 'WATER' in token_name:
        return 'blue'
    if 'MOUNTAIN' in token_name:
        return 'grey'

if __name__ == "__main__":
    print("*** ENTIRELY NEW RUN ***")
    session_state = st.session_state

# THIS IS INITIAL SETUP AND NEED TO BE DONE ONLY ONCE
    if 'app_state' not in session_state:
        session_state.app_state = 'initial_setup_started'  
        session_state.counter = 0

    st.write(f":orange[session_state]: {st.session_state.app_state}")

    # if "counter" not in st.session_state:
    if session_state.app_state == 'initial_setup_started':
        st.header("BEGINNING OF INITIAL SETUP")

        if "starting_bags_created" not in st.session_state:
            tokens.create_starting_bags_of_tokens() # at this moment there should be 2 lists of tokens: 18 WEAKNESS tokens in WEAKNESS_TOKENS_BAG and 18 tokens in TRAIL_TOKENS_BAG, both bags are already randomized/shuffled
            st.session_state.starting_bags_created = True


        # manually get one token for FOREST, WATER, MOUNTAIN to place initial monsters
        # remove those tokens from the TRAIL_TOKENS_BAG

        with st.form('Inputs'):
            t1 = st.selectbox("Choose token for FOREST monster", tokens.TRAIL_TOKENS_BAG, index=0, key = 't1_selectbox')
            t2 = st.selectbox("Choose token for FOREST monster", tokens.TRAIL_TOKENS_BAG, index=1, key = 't2_selectbox')
            t3 = st.selectbox("Choose token for FOREST monster", tokens.TRAIL_TOKENS_BAG, index=2, key = 't3_selectbox')

            if st.form_submit_button('Submit'):
                tokens.intentionally_remove_one_token_from_bag('TRAIL', t1)
                tokens.intentionally_remove_one_token_from_bag('TRAIL', t2)
                tokens.intentionally_remove_one_token_from_bag('TRAIL', t3)

                st.write('*** 3 STARTING TOKENS FOR MONSTERS WERE REMOVED FROM TOKENS BAG AND WERE PLACED ON THE BOARD***')
                print('*** 3 STARTING TOKENS FOR MONSTERS WERE REMOVED FROM TOKENS BAG AND WERE PLACED ON THE BOARD***')
                print()

                session_state.app_state = 'monster_trail_tokens_placed'

        # tokens.intentionally_remove_one_token_from_bag('TRAIL', 'TRAIL_FOREST_10')
        # my_bar.progress(percent_complete + 1 * progress_increment, text=progress_text)
        # tokens.intentionally_remove_one_token_from_bag('TRAIL', 'TRAIL_WATER_12')
        # my_bar.progress(percent_complete + 2 * progress_increment, text=progress_text)
        # tokens.intentionally_remove_one_token_from_bag('TRAIL', 'TRAIL_MOUNTAIN_11')
        # my_bar.progress(percent_complete + 3 * progress_increment, text=progress_text)

        

    if session_state.app_state == 'monster_trail_tokens_placed':
# now randomly choose 3 weakness tokens and randomly choose their locations by picking 3 TRAIL tokens that will be immediately returned to TRAIL bag later
    # FOREST MONSTER SETUP
        weakness_token = tokens.randomly_remove_one_token_from_bag('WEAKNESS', 'FOREST')
        trail_token = tokens.randomly_remove_one_token_from_bag('TRAIL', 'FOREST')
        color = get_color_for_token(weakness_token)
        print(f"*** PLACE {weakness_token} AT SPOT {trail_token}")
        st.write(f"*** PLACE :{color}[{weakness_token}] AT SPOT :{color}[{trail_token}]")
        st.toast(f"*** PLACE :{color}[{weakness_token}] AT SPOT :{color}[{trail_token}]")
        # return TRAIL FOREST token to bag
        tokens.return_token_to_bag(trail_token)
        print('-------------------------------------------------')

    # WATER MONSTER SETUP
        weakness_token = tokens.randomly_remove_one_token_from_bag('WEAKNESS', 'WATER')
        trail_token = tokens.randomly_remove_one_token_from_bag('TRAIL', 'WATER')
        color = get_color_for_token(weakness_token)
        print(f"*** PLACE {weakness_token} AT SPOT {trail_token}")
        st.write(f"*** PLACE :{color}[{weakness_token}] AT SPOT :{color}[{trail_token}]")
        st.toast(f"*** PLACE :{color}[{weakness_token}] AT SPOT :{color}[{trail_token}]")
        # return TRAIL WATER token to bag
        tokens.return_token_to_bag(trail_token)
        print('-------------------------------------------------')

    # MOUNTAIN MONSTER SETUP
        weakness_token = tokens.randomly_remove_one_token_from_bag('WEAKNESS', 'MOUNTAIN')
        trail_token = tokens.randomly_remove_one_token_from_bag('TRAIL', 'MOUNTAIN')
        color = get_color_for_token(weakness_token)
        print(f"*** PLACE {weakness_token} AT SPOT {trail_token}")
        st.write(f"*** PLACE :{color}[{weakness_token}] AT SPOT :{color}[{trail_token}]")
        st.toast(f"*** PLACE :{color}[{weakness_token}] AT SPOT :{color}[{trail_token}]")
        # return TRAIL MOUNTAIN token to bag
        tokens.return_token_to_bag(trail_token)
        print('-------------------------------------------------')

        if 'WEAKNESS_TOKENS_BAG' not in st.session_state:
            st.session_state['WEAKNESS_TOKENS_BAG'] = tokens.WEAKNESS_TOKENS_BAG

        if 'TRAIL_TOKENS_BAG' not in st.session_state:
            st.session_state['TRAIL_TOKENS_BAG'] = tokens.TRAIL_TOKENS_BAG

        if 'REMOVED_WEAKNESS_TOKENS_BAG' not in st.session_state:
            st.session_state['REMOVED_WEAKNESS_TOKENS_BAG'] = tokens.REMOVED_WEAKNESS_TOKENS_BAG

        if 'REMOVED_TRAIL_TOKENS_BAG' not in st.session_state:
            st.session_state['REMOVED_TRAIL_TOKENS_BAG'] = tokens.REMOVED_TRAIL_TOKENS_BAG

        if 'most_recently_chosen_token' not in st.session_state:
            st.session_state['most_recently_chosen_token'] = 'None'

        if 'logs_list' not in st.session_state:
            st.session_state['logs_list'] = []

        st.write(st.session_state.app_state)
        if st.button("Weakness tokens placed. Continue to next step"):
            session_state.app_state = 'monster_weakness_tokens_placed'
            st.write(st.session_state.app_state)
            st.rerun()
            st.write(st.session_state.app_state)

    # print(tokens.WEAKNESS_TOKENS_BAG)
    # print(tokens.TRAIL_TOKENS_BAG)

    if session_state.app_state == 'monster_weakness_tokens_placed':
        print("*************************************************")
        
        st.session_state.counter += 1

        st.header("GAME READY TO PLAY")
        
        a, b = st.columns(2)
        c, d = st.columns(2)
        a.metric(label = "\\# of tokens left in WEAKNESS_TOKENS_BAG", value = len(st.session_state['WEAKNESS_TOKENS_BAG']))
        b.metric(label = "\\# of tokens removed from WEAKNESS_TOKENS_BAG", value = len(st.session_state['REMOVED_WEAKNESS_TOKENS_BAG']))
        c.metric(label = "\\# of tokens left in TRAIL_TOKENS_BAG", value = len(st.session_state['TRAIL_TOKENS_BAG']))
        d.metric(label = "\\# of tokens removed from TRAIL_TOKENS_BAG", value = len(st.session_state['REMOVED_TRAIL_TOKENS_BAG']))
        
        #After initial setup it is time to allow users to click buttons
        #TODO: randomly_remove_one_token_from_bag in case of quests, new monsters ETC
        #TODO: return_token_to_bag in case of finished quests, defeated monsters ETC

        st.subheader('REMOVE TOKEN FROM BAG', divider = "green")
        col1, col2, col3, col4 = st.columns(4, vertical_alignment = 'center')
        with col1:
            remove_type = st.radio("Choose token type for randomly selected token:", ('TRAIL', 'WEAKNESS'))
        with col2:
            remove_territory_type = st.radio("Choose territory type:", ('FOREST', 'WATER', 'MOUNTAIN'))
        with col3:
            randomly_remove_one_token_from_bag = st.button('Randomly get token from corresponding bag')
        if randomly_remove_one_token_from_bag:
            most_recently_chosen_token = tokens.randomly_remove_one_token_from_bag(remove_type, remove_territory_type)
            st.session_state['most_recently_chosen_token'] = most_recently_chosen_token
            st.rerun()
        with col4:
            try:
                st.write(f"Most recently chosen token: {st.session_state.most_recently_chosen_token}")
            except NameError:
                st.write("No token was removed yet")

        st.subheader("RETURN TOKEN TO BAG", divider = "green")
        col1, col2, col3 = st.columns(3, vertical_alignment = 'bottom')
        with col1:
            return_type = st.radio("Choose token type for token to be returned:", ('TRAIL', 'WEAKNESS'))
            if return_type == 'WEAKNESS':
                tokens_bag = tokens.REMOVED_WEAKNESS_TOKENS_BAG #TODO: figure out how to sort this list
            else:
                tokens_bag = tokens.REMOVED_TRAIL_TOKENS_BAG #TODO: figure out how to sort this list
        with col2:
            token_to_return = st.selectbox(
                "Choose token to return",
                tokens_bag,
                index=0
            )
        with col3:
            if token_to_return is None:
                return_token_to_bag = st.button('Return token to corresponding bag', disabled = True)
            else:
                return_token_to_bag = st.button('Return token to corresponding bag', disabled = False)

        if return_token_to_bag:
            tokens.return_token_to_bag(token_to_return)
            color = get_color_for_token(token_to_return)
            st.toast(f"Token :{color}[{token_to_return}] has been returned to corresponding bag.", icon=":material/info:")
            st.rerun()

        st.button("Run it again")
        print("*** END OF RUN ***")
        quit()

    # debug
        token = tokens.Token('TRAIL', 'WATER', 1)
        token.print_definition()
        