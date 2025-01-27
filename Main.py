import modules.tokens as tokens
import streamlit as st

global most_recently_chosen_token
global session_state
global add_skellige

def page_config():
    # st.set_option("theme.base", 'dark')
    path_to_logo = r"assets/images/the_witcher_3__wild_hunt_logo.jpg"
    st.set_page_config(
        page_title = "Witcher: Old World - Board Game",
        layout = "wide",
        initial_sidebar_state = 'collapsed', #"expanded",
        page_icon = path_to_logo
    )

    sidebar_logo = path_to_logo
    main_body_logo = path_to_logo
    st.logo(sidebar_logo, size="large", icon_image=main_body_logo)

    with st.sidebar:
        st.image(path_to_logo)

        st.markdown(
        '<a href="mailto:elpietruch@gmail.com">Contact me!</a>',
        unsafe_allow_html=True
        )

        st.caption('''version: 0.1''')

def sort_tokens_alphabetically(e):
    return e.token_id

def set_app_state_to_monster_weakness_tokens_placed():
    st.session_state.app_state = 'monster_weakness_tokens_placed'

def check_number_of_tokens_left_in_bag(remove_type, remove_territory_type = None) -> int:
    if remove_territory_type is None:
        if 'WEAKNESS' in remove_type:
            return len(tokens.WEAKNESS_TOKENS_BAG)
        else:
            return len(tokens.TRAIL_TOKENS_BAG)

    else:
        if 'WEAKNESS' in remove_type:
            return sum(1 for i in tokens.WEAKNESS_TOKENS_BAG if i.territory_type == remove_territory_type)
        else:
            return sum(1 for i in tokens.TRAIL_TOKENS_BAG if i.territory_type == remove_territory_type)
    
@st.dialog("ℹ️ INFO", width= 'large')
def show_modal_with_info():
    st.info("Welcome to the Witcher Old World - Board Game helper :material/waving_hand:", icon= 'ℹ️')
    st.write("It should alleviate some of the pain connected to dealing with tokens by allowing you to:")  
    st.markdown(
        '''
            * ***randomly*** pick tokens from bags
            * return ***selected*** tokens to corresponding bags
            * intentionally draw ***selected*** tokens from bags
        ''')
    st.write("Structure of the APP:")
    st.markdown(
        '''
        * 1. INITIAL SETUP FOR MONSTERS (:material/travel_explore: TRAIL AND :material/wounds_injuries: WEAKNESS TOKENS)
            * 1a. :material/travel_explore: TRAIL TOKENS SETUP FOR INITIAL MONSTERS
            * 1b. PLACING :material/wounds_injuries: WEAKNESS TOKENS FOR INITIAL MONSTERS
        * 2. INITIAL TOKENS ARE SET, GAME READY TO PLAY :material/swords:
        ''')

def check_if_all_lists_are_empty() -> bool:
    if len(tokens.TRAIL_TOKENS_BAG) == 0 and len(tokens.WEAKNESS_TOKENS_BAG) == 0 and len(tokens.REMOVED_TRAIL_TOKENS_BAG) == 0 and len(tokens.REMOVED_WEAKNESS_TOKENS_BAG) == 0:
        return True
    else:
        return False

def print_tokens_as_images(TRAIL_TOKENS_BAG_list_name: str, WEAKNESS_TOKENS_BAG_list_name: str, REMOVED_TRAIL_TOKENS_BAG_list_name: str, REMOVED_WEAKNESS_TOKENS_BAG_list_name: str) -> None:
    st.subheader("SHOW ALL TOKENS IN BAGS", divider = "green")
    tab1, tab2, tab3, tab4 = st.tabs(
        [":material/travel_explore: TRAIL_TOKENS left in bag", ":material/wounds_injuries: WEAKNESS_TOKENS left in bag", "removed :material/travel_explore: TRAIL TOKENS", "removed :material/wounds_injuries: WEAKNESS TOKENS"]
        )
    with tab1:
        with st.expander("Show all :material/travel_explore: TRAIL TOKENS in bag:"):
            show_all_tokens_from_list(TRAIL_TOKENS_BAG_list_name)
    with tab2:
        with st.expander("Show all :material/wounds_injuries: WEAKNESS TOKENS in bag:"):
            show_all_tokens_from_list(WEAKNESS_TOKENS_BAG_list_name)
    with tab3:
        with st.expander("Show all removed :material/travel_explore: TRAIL TOKENS:"):
            show_all_tokens_from_list(REMOVED_TRAIL_TOKENS_BAG_list_name)
    with tab4:
        with st.expander("Show all removed :material/wounds_injuries: WEAKNESS TOKENS:"):
            show_all_tokens_from_list(REMOVED_WEAKNESS_TOKENS_BAG_list_name)
    pass

def show_all_tokens_from_list(list_name: str):
    if list_name == 'WEAKNESS_TOKENS_BAG':
        list_to_print = tokens.WEAKNESS_TOKENS_BAG
    elif list_name == 'TRAIL_TOKENS_BAG':
        list_to_print =  tokens.TRAIL_TOKENS_BAG
    elif list_name == 'REMOVED_WEAKNESS_TOKENS_BAG':
        list_to_print = tokens.REMOVED_WEAKNESS_TOKENS_BAG
    elif list_name == 'REMOVED_TRAIL_TOKENS_BAG':
        list_to_print = tokens.REMOVED_TRAIL_TOKENS_BAG
    else:
        st.write("Wrong list name")
        return
    
    list_to_print.sort(key = sort_tokens_alphabetically)
    counter = 1
    col1, col2, col3, col4, col5 = st.columns(5)
    for token in list_to_print:
        if counter % 5 == 1:
            col_name = col1
        elif counter % 5 == 2:
            col_name = col2
        elif counter % 5 == 3:
            col_name = col3
        elif counter % 5 == 4:
            col_name = col4
        else:
            col_name = col5

        with col_name:
            st.image(token.token_img_path, caption = token.token_fullname)
            counter += 1

def clear_all_tokens_lists() -> None:
    tokens.TRAIL_TOKENS_BAG = []
    tokens.WEAKNESS_TOKENS_BAG = []
    tokens.REMOVED_TRAIL_TOKENS_BAG = []
    tokens.REMOVED_WEAKNESS_TOKENS_BAG = []

def nuclear_reset() -> None:
    clear_all_tokens_lists()
    st.cache_data.clear()
    st.cache_resource.clear()
    st.session_state.clear()
    for key in st.session_state.keys():
        del st.session_state[key]

def initial_setup() -> None:
    if 'app_state' not in st.session_state:
        st.cache_data.clear()
        st.cache_resource.clear()
        st.session_state.app_state = 'initial_setup_started'  
        st.session_state.counter = 0
        show_modal_with_info()

    if 'most_recently_chosen_token' not in st.session_state:
        st.session_state['most_recently_chosen_token'] = 'None'
    pass

def decide_if_Skellige_should_be_included_and_create_bags():
    placeholder_skellige = st.empty()
    with placeholder_skellige.container():
        with st.form('Skellige inclusion?'):
            st.write("Skellige tokens are special :material/travel_explore: TRAIL TOKENS that can be included in the game. Do you want to include them?")

            col1, col2 = st.columns(2)
            with col1:
                st.image(r'assets/images/Skellige.png')
            with col2:
                add_skellige_bool = st.checkbox("Include Skellige :material/travel_explore: TRAIL TOKENS in the game", key = 'add_skellige_checkbox')
                skellige_submitted = st.form_submit_button('Confirm choice about Skellige inclusion', help = "Click to confirm your choice about Skellige tokens inclusion")

            if skellige_submitted:
                tokens.create_starting_bags_of_tokens(add_skellige_bool) # at this moment there should be 2 lists of tokens: 18 WEAKNESS tokens in WEAKNESS_TOKENS_BAG and 18 tokens in TRAIL_TOKENS_BAG, both bags are already randomized/shuffled
                st.session_state.starting_bags_created = True
                # DONE hide st.form by using st.empty()
                placeholder_skellige.empty()
    pass

def create_info_buttons_and_do_page_config() -> None:
    page_config()
    print("*** ENTIRELY NEW RUN - STARTING FROM TOP OF THE 1_Main SCRIPT ***")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.button(label= ':material/help: INFO', on_click = show_modal_with_info)
    with col5:
        st.button(label= ':material/history: NUCLEAR RESET. RERUN WHOLE APP', on_click = nuclear_reset, type="primary", help = "This will trigger full nuclear reset of the app. Use it only if you are sure you want to reset the app to the initial state.")
    pass

def place_starting_trail_tokens_for_monsters() -> None:
    placeholder_1a = st.empty()
    with placeholder_1a.container():
        st.subheader("1a. :material/travel_explore: TRAIL TOKENS SETUP FOR INITIAL MONSTERS")
        with st.form('Inputs'):
            st.subheader(':orange[MANUALLY] choose 3 :material/travel_explore: TRAIL TOKENS from physical board game tokens and place them on 3 monsters spots on board. Chosen tokens will be removed from :material/travel_explore: TRAIL TOKENS bag for now (but will return after monster defeat).')
            forest_trail_tokens_list = list(filter(lambda token_names: 'FOREST' in token_names.token_fullname , tokens.TRAIL_TOKENS_BAG))
            forest_trail_tokens_list.sort(key = sort_tokens_alphabetically)

            water_trail_tokens_list = list(filter(lambda token_names: 'WATER' in token_names.token_fullname , tokens.TRAIL_TOKENS_BAG))
            water_trail_tokens_list.sort(key = sort_tokens_alphabetically)
            mountain_trail_tokens_list = list(filter(lambda token_names: 'MOUNTAIN' in token_names.token_fullname , tokens.TRAIL_TOKENS_BAG))
            mountain_trail_tokens_list.sort(key = sort_tokens_alphabetically)

            t1 = st.selectbox("Choose initial token for :green[FOREST] monster", forest_trail_tokens_list, index=0, key = 't1_selectbox')
            t2 = st.selectbox("Choose initial token for :blue[WATER] monster", water_trail_tokens_list, index=0, key = 't2_selectbox')
            t3 = st.selectbox("Choose initial token for :grey[MOUNTAIN] monster", mountain_trail_tokens_list, index=0, key = 't3_selectbox')

            disabled = check_if_all_lists_are_empty() # or t1 is None or t2 is None or t3 is None
            submitter = st.form_submit_button('Proceed to :material/wounds_injuries: WEAKNESS TOKENS setup', help = "Click to remove selected tokens from TRAIL tokens bag and :orange[manually] place them on the board", disabled = disabled)

            if submitter:
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
                st.session_state.initial_weakness_tokens_removed = False
        # DONE hide st.form by using st.empty()
                placeholder_1a.empty()
    pass

def place_starting_weakness_tokens_from_monsters() -> None:
    st.subheader("1b. PLACING :material/wounds_injuries: WEAKNESS TOKENS FOR INITIAL MONSTERS")
    
    if st.session_state.initial_weakness_tokens_removed == False:
    # FOREST MONSTER SETUP
        weakness_token = tokens.randomly_remove_one_token_from_bag('WEAKNESS', 'FOREST')
        trail_token = tokens.randomly_remove_one_token_from_bag('TRAIL', 'FOREST')
        color = tokens.get_color_for_token(weakness_token)
        tokens.return_token_to_bag(trail_token)
        # TRAIL FOREST token returned to bag
        print(f"*** PLACE {weakness_token} AT SPOT {trail_token}")
        st.session_state.forest_monster_weakness_placement_string = f"*** :orange[MANUALLY] PLACE :{color}[:material/wounds_injuries: {weakness_token}] AT SPOT :{color}[:material/travel_explore: {trail_token}]"
        st.write(st.session_state.forest_monster_weakness_placement_string)
        print('-------------------------------------------------')

    # WATER MONSTER SETUP
        weakness_token = tokens.randomly_remove_one_token_from_bag('WEAKNESS', 'WATER')
        trail_token = tokens.randomly_remove_one_token_from_bag('TRAIL', 'WATER')
        color = tokens.get_color_for_token(weakness_token)
        tokens.return_token_to_bag(trail_token)
        # TRAIL WATER token returned to bag
        print(f"*** PLACE {weakness_token} AT SPOT {trail_token}")
        st.session_state.water_monster_weakness_placement_string = f"*** :orange[MANUALLY] PLACE :{color}[:material/wounds_injuries: {weakness_token}] AT SPOT :{color}[:material/travel_explore: {trail_token}]"
        st.write(st.session_state.water_monster_weakness_placement_string)
        print('-------------------------------------------------')

    # MOUNTAIN MONSTER SETUP
        weakness_token = tokens.randomly_remove_one_token_from_bag('WEAKNESS', 'MOUNTAIN')
        trail_token = tokens.randomly_remove_one_token_from_bag('TRAIL', 'MOUNTAIN')
        color = tokens.get_color_for_token(weakness_token)
        tokens.return_token_to_bag(trail_token)
        # TRAIL MOUNTAIN token returned to bag
        print(f"*** PLACE {weakness_token} AT SPOT {trail_token}")
        st.session_state.mountain_monster_weakness_placement_string = f"*** :orange[MANUALLY] PLACE :{color}[:material/wounds_injuries: {weakness_token}] AT SPOT :{color}[:material/travel_explore: {trail_token}]"
        st.write(st.session_state.mountain_monster_weakness_placement_string)
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

    if st.session_state.initial_weakness_tokens_removed == True:
        st.write(st.session_state.forest_monster_weakness_placement_string)
        st.write(st.session_state.water_monster_weakness_placement_string)
        st.write(st.session_state.mountain_monster_weakness_placement_string)
    
    # ?: WTF DOES THIS BUTTON CHANGE APP_STATE WITHOUT EVEN BEING CLICKED ON?
    st.button(":material/wounds_injuries: Weakness tokens placed. Continue to next step", key = 'weakness_tokens_placed', on_click= set_app_state_to_monster_weakness_tokens_placed, help = "Click to finish initial setup for monsters and continue to the next step")

    st.session_state.initial_weakness_tokens_removed = True

# FIXME PROBABLY REDUNTANT
    if st.session_state.app_state == 'monster_weakness_tokens_placed':
        st.write(st.session_state.app_state)
        st.rerun()
    pass

def show_metrics() -> None:
    st.session_state.counter += 1

    st.header("2. INITIAL TOKENS ARE SET, GAME READY TO PLAY :material/swords:")
    
    a, b = st.columns(2)
    c, d = st.columns(2)
    a.metric(label = "\\# of tokens **left in** :material/travel_explore: TRAIL_TOKENS_BAG", value = len(st.session_state['TRAIL_TOKENS_BAG']))
    b.metric(label = "\\# of tokens **removed from** :material/travel_explore: TRAIL_TOKENS_BAG", value = len(st.session_state['REMOVED_TRAIL_TOKENS_BAG']))
    c.metric(label = "\\# of tokens **left in** :material/wounds_injuries: WEAKNESS_TOKENS_BAG", value = len(st.session_state['WEAKNESS_TOKENS_BAG']))
    d.metric(label = "\\# of tokens **removed from** :material/wounds_injuries: WEAKNESS_TOKENS_BAG", value = len(st.session_state['REMOVED_WEAKNESS_TOKENS_BAG']))
    pass

def render_and_print_first_section_randomly_remove_one_token_from_bag() -> None:
    pass

def render_and_print_second_section_intentionally_return_one_token_to_bag() -> None:
    pass

def render_and_print_third_section_intentionally_draw_one_token_from_bag() -> None:
    pass


if __name__ == "__main__":
    create_info_buttons_and_do_page_config()

#? THIS IS INITIAL SETUP AND NEEDS TO BE DONE ONLY ONCE
    initial_setup()

    if (st.session_state.app_state == 'initial_setup_started' or st.session_state.counter == 0) and st.session_state.app_state != 'initial_weakness_tokens_removed' and st.session_state.app_state != 'monster_weakness_tokens_placed':
        st.header("1. INITIAL SETUP FOR MONSTERS (:material/travel_explore: TRAIL AND :material/wounds_injuries: WEAKNESS TOKENS)")

        if "starting_bags_created" not in st.session_state:
            st.write()
            
            # this is used to reset the app and overcome glitch when app didn't want to rerun properly after web refresh
            if st.session_state.counter == 0:
                clear_all_tokens_lists()

#to overcome selfresfreshing Streamlit web "feature" try to start this function only if all lists are empty
            if check_if_all_lists_are_empty(): 
                # ask about Skellige tokens inclusion
                decide_if_Skellige_should_be_included_and_create_bags()

        if "starting_bags_created" in st.session_state and st.session_state.starting_bags_created == True and st.session_state.app_state not in ('monster_weakness_tokens_placed', 'monster_trail_tokens_placed'):
            # manually get one token for FOREST, WATER, MOUNTAIN to place initial monsters
            # remove those tokens from the TRAIL_TOKENS_BAG
            place_starting_trail_tokens_for_monsters()

    if st.session_state.app_state == 'monster_trail_tokens_placed': # and st.session_state.initial_weakness_tokens_removed is not True:
# now randomly choose 3 weakness tokens and randomly choose their locations by picking 3 TRAIL tokens that will be immediately returned to TRAIL bag
        place_starting_weakness_tokens_from_monsters()

    if st.session_state.app_state == 'monster_weakness_tokens_placed':
        show_metrics()

#? After initial setup it is time to allow users to click buttons
    # DONE: ADD FIRST SECTION: randomly_remove_one_token_from_bag in case of quests, new monsters ETC
        render_and_print_first_section_randomly_remove_one_token_from_bag()
        st.subheader('DRAW :orange[RANDOM] TOKEN FROM BAG - :orange[MANUALLY] PLACE THIS TOKEN ON BOARD OR USE IT FOR QUESTS ETC', divider = "green")

        col1, col2, col3, col4 = st.columns(4, vertical_alignment = 'center')
        with col1:
            remove_randomly_type = st.radio("Choose token type:", (':material/travel_explore: TRAIL', ':material/wounds_injuries: WEAKNESS'), key = 'remove_type_radio')

        with col2:
            remove_randomly_territory_type = st.radio("Choose territory type:", ('FOREST', 'WATER', 'MOUNTAIN'))
        
        with col3:
            # DONE: disable this button if number of remove_type x remove_territory_type tokens in bag is 0
            remove_randomly_disabled = check_number_of_tokens_left_in_bag(remove_randomly_type, remove_randomly_territory_type) <= 0
            color = tokens.get_color_for_token(remove_randomly_territory_type)
            randomly_remove_one_token_from_bag = st.button(f'Randomly draw :{color}[{remove_randomly_type} {remove_randomly_territory_type}] token from corresponding bag', disabled = remove_randomly_disabled)
        if randomly_remove_one_token_from_bag:
            most_recently_chosen_token = tokens.randomly_remove_one_token_from_bag(remove_randomly_type, remove_randomly_territory_type)
            st.session_state['most_recently_chosen_token'] = most_recently_chosen_token
            st.rerun()

        with col4:
            if st.session_state.most_recently_chosen_token == 'None' or st.session_state.most_recently_chosen_token is None:
                st.write("No token was removed yet")
            else:
                color = tokens.get_color_for_token(st.session_state.most_recently_chosen_token)
                if 'WEAKNESS' in st.session_state.most_recently_chosen_token:
                    icon = ':material/wounds_injuries:'
                else:
                    icon = ':material/travel_explore:'
                st.write(f"Most recently chosen token: :{color}[{icon} {st.session_state.most_recently_chosen_token}]")


    # DONE: ADD SECOND SECTION: return_token_to_bag in case of finished quests, defeated monsters ETC
        st.subheader("RETURN :orange[SELECTED] TOKEN TO BAG", divider = "green")
        col1, col2, col3 = st.columns(3, vertical_alignment = 'bottom')

        with col1:
            return_type = st.radio("Choose token type:", (':material/travel_explore: TRAIL', ':material/wounds_injuries: WEAKNESS'), key = 'return_type_radio')
            if 'WEAKNESS' in return_type:
                return_tokens_bag = tokens.REMOVED_WEAKNESS_TOKENS_BAG #TODO: figure out how to sort this list
                icon = ':material/wounds_injuries:'
            else:
                return_tokens_bag = tokens.REMOVED_TRAIL_TOKENS_BAG #TODO: figure out how to sort this list
                icon = ':material/travel_explore:'

        with col2:
            token_to_return = st.selectbox(
                f"Choose {return_type} token to return:",
                return_tokens_bag, #.sort(key = sort_tokens_alphabetically),
                index=0
            )
        with col3:
            if token_to_return is None:
                return_token_to_bag = st.button(f'Return selected {return_type} token to corresponding bag', disabled = True)
            else:
                return_token_to_bag = st.button(f'Return selected {return_type} token to corresponding bag', disabled = False)

        if return_token_to_bag:
            tokens.return_token_to_bag(token_to_return)
            color = tokens.get_color_for_token(token_to_return)
            st.toast(f"Token :{color}[{icon} {token_to_return}] has been returned to corresponding bag.", icon=":material/info:")
            st.rerun()

    # DONE: ADD THIRD SECTION: INTENTIONALLY DRAW SELECTED TOKEN FROM BAG
        st.subheader("INTENTIONALLY DRAW :orange[SELECTED] TOKEN FROM BAG", divider = "green")
        
        col1, col2, col3 = st.columns(3, vertical_alignment = 'bottom')
        with col1:
            remove_intentionally_type = st.radio("Choose token type:", (':material/travel_explore: TRAIL', ':material/wounds_injuries: WEAKNESS'), key = 'remove_selected_type_radio')
            if 'WEAKNESS' in remove_intentionally_type:
                draw_tokens_bag = tokens.WEAKNESS_TOKENS_BAG #TODO: figure out how to sort this list
                icon = ':material/wounds_injuries:'
            else:
                draw_tokens_bag = tokens.TRAIL_TOKENS_BAG #TODO: figure out how to sort this list
                icon = ':material/travel_explore:'

        with col2:
            token_to_draw = st.selectbox(
                f"Choose {remove_intentionally_type} token to draw:",
                draw_tokens_bag, #.sort(key = sort_tokens_alphabetically),
                index=0
            )

        with col3:
            disabled = check_number_of_tokens_left_in_bag(remove_intentionally_type) <= 0
            color = tokens.get_color_for_token(token_to_draw)
            if color is not None:
                button_label = f'Intentionally draw :{color}[{icon} {token_to_draw}] token from corresponding bag'
            else:
                button_label = f'There are no {icon} tokens left in the bag'
            intentionally_remove_one_token_from_bag = st.button(button_label, disabled = disabled)
        if intentionally_remove_one_token_from_bag:
            most_recently_chosen_token = tokens.intentionally_remove_one_token_from_bag(remove_intentionally_type, token_to_draw)
            st.rerun()


        # DONE PRINT ALL TOKENS AS IMAGES
        print_tokens_as_images('TRAIL_TOKENS_BAG', 'WEAKNESS_TOKENS_BAG', 'REMOVED_TRAIL_TOKENS_BAG', 'REMOVED_WEAKNESS_TOKENS_BAG')

        print("*** END OF RUN ***")