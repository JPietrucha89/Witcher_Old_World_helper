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
    # st.set_option("theme.base", 'dark')

    st.set_page_config(
        page_title="Witcher 3: Wild Hunt - Board Game", 
        layout="wide", 
        initial_sidebar_state= 'collapsed', #"expanded",
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

        st.caption('''version: 0.1''')

def sort_tokens_alphabetically(e):
    return e.token_id

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

def set_app_state_to_monster_weakness_tokens_placed():
    st.session_state.app_state = 'monster_weakness_tokens_placed'

def check_number_of_tokens_left_in_bag(remove_type, remove_territory_type):
    if 'WEAKNESS' in remove_type:
        return sum(1 for i in tokens.WEAKNESS_TOKENS_BAG if i.territory_type == remove_territory_type)
    else:
        return sum(1 for i in tokens.TRAIL_TOKENS_BAG if i.territory_type == remove_territory_type)

@st.dialog("ℹ️ INFO", width= 'large')
def show_modal_with_info():
    st.info("Welcome to the Witcher Old World - Board Game helper. It should alleviate some of the pain connected to dealing with tokens by allowing you to: randomly pick tokens from bags, return tokens to corresponding bags", icon= 'ℹ️')
    st.write("Structure of the app:") #, key = 'welcome_dialog')
    st.markdown(
        '''
        * 1. INITIAL SETUP FOR MONSTERS (:material/travel_explore: TRAIL AND :material/wounds_injuries: WEAKNESS TOKENS)
            * 1a. :material/travel_explore: TRAIL TOKENS SETUP FOR INITIAL MONSTERS
            - 1b. PLACING :material/wounds_injuries: WEAKNESS TOKENS FOR INITIAL MONSTERS
        + 2. INITIAL TOKENS ARE SET, GAME READY TO PLAY
        ''')
    
#? DONE add button/modal form with Info about the APP
#!FIXME:somehow working but it breaks between steps 1a and 1b XD

#? DONE include description for all of the stages of the APP (1. 2. 3. etc)
if __name__ == "__main__":
    page_config()
    print("*** ENTIRELY NEW RUN ***")
    session_state = st.session_state
    st.button(label= ':material/help: INFO', on_click = show_modal_with_info)
#? THIS IS INITIAL SETUP AND NEEDS TO BE DONE ONLY ONCE
    if 'app_state' not in st.session_state:
        st.cache_data.clear()
        st.cache_resource.clear()
        st.session_state.app_state = 'initial_setup_started'  
        st.session_state.counter = 0

    if 'most_recently_chosen_token' not in st.session_state:
        st.session_state['most_recently_chosen_token'] = 'None'

    # st.write(f":orange[session_state]: {st.session_state.app_state}")
    # st.write(f":orange[session_state]: {st.session_state.most_recently_chosen_token}")

    # if "counter" not in st.session_state:
    if st.session_state.app_state == 'initial_setup_started':
        st.header("1. INITIAL SETUP FOR MONSTERS (:material/travel_explore: TRAIL AND :material/wounds_injuries: WEAKNESS TOKENS)")

        if "starting_bags_created" not in st.session_state:
            show_modal_with_info()
            st.write()
            tokens.create_starting_bags_of_tokens() # at this moment there should be 2 lists of tokens: 18 WEAKNESS tokens in WEAKNESS_TOKENS_BAG and 18 tokens in TRAIL_TOKENS_BAG, both bags are already randomized/shuffled
            st.session_state.starting_bags_created = True

        # manually get one token for FOREST, WATER, MOUNTAIN to place initial monsters
        # remove those tokens from the TRAIL_TOKENS_BAG
        placeholder_1a = st.empty()
        with placeholder_1a.container():
            st.subheader("1a. :material/travel_explore: TRAIL TOKENS SETUP FOR INITIAL MONSTERS")
            with st.form('Inputs'):
                st.subheader('Choose 3 :material/travel_explore: TRAIL TOKENS for initial monsters. They will be removed from corresponding bag.')
                forest_trail_tokens_list = list(filter(lambda token_names: 'FOREST' in token_names.token_fullname , tokens.TRAIL_TOKENS_BAG))
                forest_trail_tokens_list.sort(key = sort_tokens_alphabetically)

                water_trail_tokens_list = list(filter(lambda token_names: 'WATER' in token_names.token_fullname , tokens.TRAIL_TOKENS_BAG))
                water_trail_tokens_list.sort(key = sort_tokens_alphabetically)
                mountain_trail_tokens_list = list(filter(lambda token_names: 'MOUNTAIN' in token_names.token_fullname , tokens.TRAIL_TOKENS_BAG))
                mountain_trail_tokens_list.sort(key = sort_tokens_alphabetically)

                t1 = st.selectbox("Choose token for :green[FOREST] monster", forest_trail_tokens_list, index=0, key = 't1_selectbox')
                t2 = st.selectbox("Choose token for :blue[WATER] monster", water_trail_tokens_list, index=0, key = 't2_selectbox')
                t3 = st.selectbox("Choose token for :grey[MOUNTAIN] monster", mountain_trail_tokens_list, index=0, key = 't3_selectbox')

                submitter = st.form_submit_button('Proceed to :material/wounds_injuries: WEAKNESS TOKENS setup', help = "Click to remove selected tokens from TRAIL tokens bag and place them on the board")

                if submitter: #st.form_submit_button('Submit'):
                    tokens.intentionally_remove_one_token_from_bag('TRAIL', t1)
                    tokens.intentionally_remove_one_token_from_bag('TRAIL', t2)
                    tokens.intentionally_remove_one_token_from_bag('TRAIL', t3)
                    
                    #clear some keys from session_state
                    del st.session_state.t1_selectbox
                    del st.session_state.t2_selectbox
                    del st.session_state.t3_selectbox

                    st.write('*** 3 STARTING :material/travel_explore: TRAIL TOKENS FOR MONSTERS WERE REMOVED FROM TRAIL TOKENS BAG AND WERE PLACED ON THE BOARD***')
                    print('*** 3 STARTING TOKENS FOR MONSTERS WERE REMOVED FROM TRAIL TOKENS BAG AND WERE PLACED ON THE BOARD***')
                    print()

                    st.session_state.app_state = 'monster_trail_tokens_placed'
            #? DONE hide st.form by using st.empty()
                    placeholder_1a.empty()


        

    if st.session_state.app_state == 'monster_trail_tokens_placed' and 'initial_weakness_tokens_removed' not in st.session_state:
# now randomly choose 3 weakness tokens and randomly choose their locations by picking 3 TRAIL tokens that will be immediately returned to TRAIL bag later
        st.subheader("1b. PLACING :material/wounds_injuries: WEAKNESS TOKENS FOR INITIAL MONSTERS")
    # FOREST MONSTER SETUP
        weakness_token = tokens.randomly_remove_one_token_from_bag('WEAKNESS', 'FOREST')
        trail_token = tokens.randomly_remove_one_token_from_bag('TRAIL', 'FOREST')
        color = get_color_for_token(weakness_token)
        tokens.return_token_to_bag(trail_token)
        # TRAIL FOREST token returned to bag
        print(f"*** PLACE {weakness_token} AT SPOT {trail_token}")
        st.write(f"*** PLACE :{color}[:material/wounds_injuries: {weakness_token}] AT SPOT :{color}[:material/travel_explore: {trail_token}]")
        st.toast(f"*** PLACE :{color}[:material/wounds_injuries: {weakness_token}] AT SPOT :{color}[:material/travel_explore: {trail_token}]")
        print('-------------------------------------------------')

    # WATER MONSTER SETUP
        weakness_token = tokens.randomly_remove_one_token_from_bag('WEAKNESS', 'WATER')
        trail_token = tokens.randomly_remove_one_token_from_bag('TRAIL', 'WATER')
        color = get_color_for_token(weakness_token)
        tokens.return_token_to_bag(trail_token)
        # TRAIL WATER token returned to bag
        print(f"*** PLACE {weakness_token} AT SPOT {trail_token}")
        st.write(f"*** PLACE :{color}[:material/wounds_injuries: {weakness_token}] AT SPOT :{color}[:material/travel_explore: {trail_token}]")
        st.toast(f"*** PLACE :{color}[:material/wounds_injuries: {weakness_token}] AT SPOT :{color}[:material/travel_explore: {trail_token}]")
        print('-------------------------------------------------')

    # MOUNTAIN MONSTER SETUP
        weakness_token = tokens.randomly_remove_one_token_from_bag('WEAKNESS', 'MOUNTAIN')
        trail_token = tokens.randomly_remove_one_token_from_bag('TRAIL', 'MOUNTAIN')
        color = get_color_for_token(weakness_token)
        tokens.return_token_to_bag(trail_token)
        # TRAIL MOUNTAIN token returned to bag
        print(f"*** PLACE {weakness_token} AT SPOT {trail_token}")
        st.write(f"*** PLACE :{color}[:material/wounds_injuries: {weakness_token}] AT SPOT :{color}[:material/travel_explore: {trail_token}]")
        st.toast(f"*** PLACE :{color}[:material/wounds_injuries: {weakness_token}] AT SPOT :{color}[:material/travel_explore: {trail_token}]")
        print('-------------------------------------------------')

        if 'WEAKNESS_TOKENS_BAG' not in st.session_state:
            st.session_state['WEAKNESS_TOKENS_BAG'] = tokens.WEAKNESS_TOKENS_BAG

        if 'TRAIL_TOKENS_BAG' not in st.session_state:
            st.session_state['TRAIL_TOKENS_BAG'] = tokens.TRAIL_TOKENS_BAG

        if 'REMOVED_WEAKNESS_TOKENS_BAG' not in st.session_state:
            st.session_state['REMOVED_WEAKNESS_TOKENS_BAG'] = tokens.REMOVED_WEAKNESS_TOKENS_BAG

        if 'REMOVED_TRAIL_TOKENS_BAG' not in st.session_state:
            st.session_state['REMOVED_TRAIL_TOKENS_BAG'] = tokens.REMOVED_TRAIL_TOKENS_BAG

        if 'logs_list' not in st.session_state:
            st.session_state['logs_list'] = []

        
        #! WTF DOES THIS BUTTON CHANGE APP_STATE WITHOUT EVEN BEING CLICKED ON?
        st.button(":material/wounds_injuries: Weakness tokens placed. Continue to next step", key = 'weakness_tokens_placed', on_click= set_app_state_to_monster_weakness_tokens_placed, help = "Click to continue to the next step")

        st.session_state.initial_weakness_tokens_removed = True

        if st.session_state.app_state == 'monster_weakness_tokens_placed':
            # st.session_state.app_state = 'monster_weakness_tokens_placed'
            st.write(st.session_state.app_state)
            st.rerun()

    # print(tokens.WEAKNESS_TOKENS_BAG)
    # print(tokens.TRAIL_TOKENS_BAG)

    if st.session_state.app_state == 'monster_weakness_tokens_placed':
        # print("*************************************************")
        
        st.session_state.counter += 1

        st.header("2. INITIAL TOKENS ARE SET, GAME READY TO PLAY :material/swords:")
        
        a, b = st.columns(2)
        c, d = st.columns(2)
        a.metric(label = "\\# of tokens left in :material/travel_explore: TRAIL_TOKENS_BAG", value = len(st.session_state['TRAIL_TOKENS_BAG']))
        b.metric(label = "\\# of tokens removed from :material/travel_explore: TRAIL_TOKENS_BAG", value = len(st.session_state['REMOVED_TRAIL_TOKENS_BAG']))
        c.metric(label = "\\# of tokens left in :material/wounds_injuries: WEAKNESS_TOKENS_BAG", value = len(st.session_state['WEAKNESS_TOKENS_BAG']))
        d.metric(label = "\\# of tokens removed from :material/wounds_injuries: WEAKNESS_TOKENS_BAG", value = len(st.session_state['REMOVED_WEAKNESS_TOKENS_BAG']))
        
#? After initial setup it is time to allow users to click buttons
        #? DONE: randomly_remove_one_token_from_bag in case of quests, new monsters ETC
        st.subheader('DRAW RANDOM TOKEN FROM BAG', divider = "green")
        col1, col2, col3, col4 = st.columns(4, vertical_alignment = 'center')
        with col1:
            remove_type = st.radio("Choose token type:", (':material/travel_explore: TRAIL', ':material/wounds_injuries: WEAKNESS'), key = 'remove_type_radio')

        with col2:
            remove_territory_type = st.radio("Choose territory type:", ('FOREST', 'WATER', 'MOUNTAIN'))
        
        with col3:
            #?DONE: disable this button if number of remove_type x remove_territory_type tokens in bag is 0
            # st.write(check_number_of_tokens_left_in_bag(remove_type, remove_territory_type))
            disabled = check_number_of_tokens_left_in_bag(remove_type, remove_territory_type) <= 0
            color = get_color_for_token(remove_territory_type)
            randomly_remove_one_token_from_bag = st.button(f'Randomly draw :{color}[{remove_type} {remove_territory_type}] token from corresponding bag', disabled = disabled)
        if randomly_remove_one_token_from_bag:
            most_recently_chosen_token = tokens.randomly_remove_one_token_from_bag(remove_type, remove_territory_type)
            st.session_state['most_recently_chosen_token'] = most_recently_chosen_token
            st.rerun()

        with col4:
            if st.session_state.most_recently_chosen_token == 'None':
                st.write("No token was removed yet")
            else:
                color = get_color_for_token(st.session_state.most_recently_chosen_token)
                if 'WEAKNESS' in st.session_state.most_recently_chosen_token:
                    icon = ':material/wounds_injuries:'
                else:
                    icon = ':material/travel_explore:'
                st.write(f"Most recently chosen token: :{color}[{icon} {st.session_state.most_recently_chosen_token}]")


        #? DONE: return_token_to_bag in case of finished quests, defeated monsters ETC
        st.subheader("RETURN SELECTED TOKEN TO BAG", divider = "green")
        col1, col2, col3 = st.columns(3, vertical_alignment = 'bottom')

        with col1:
            return_type = st.radio("Choose token type:", (':material/travel_explore: TRAIL', ':material/wounds_injuries: WEAKNESS'), key = 'return_type_radio')
            if 'WEAKNESS' in return_type:
                tokens_bag = tokens.REMOVED_WEAKNESS_TOKENS_BAG #TODO: figure out how to sort this list
                icon = ':material/wounds_injuries:'
            else:
                tokens_bag = tokens.REMOVED_TRAIL_TOKENS_BAG #TODO: figure out how to sort this list
                icon = ':material/travel_explore:'

        with col2:
            token_to_return = st.selectbox(
                "Choose token to return:",
                tokens_bag, #.sort(key = sort_tokens_alphabetically),
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
            st.toast(f"Token :{color}[{icon} {token_to_return}] has been returned to corresponding bag.", icon=":material/info:")
            st.rerun()

        st.button("Run it again")
        print("*** END OF RUN ***")
        quit()

    # debug
        print("DEBUG AT END OF MAIN.PY")
        token = tokens.Token('TRAIL', 'WATER', 1)
        token.print_definition()
        