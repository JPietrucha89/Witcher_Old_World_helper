import random
import streamlit as st

# global TRAIL_TOKENS_BAG
# global WEAKNESS_TOKENS_BAG
# global REMOVED_TRAIL_TOKENS_BAG
# global REMOVED_WEAKNESS_TOKENS_BAG
# global most_recently_chosen_token

'''Create all global lists and variables'''
TRAIL_TOKENS_BAG = []
WEAKNESS_TOKENS_BAG = []
REMOVED_TRAIL_TOKENS_BAG = []
REMOVED_WEAKNESS_TOKENS_BAG = []
most_recently_chosen_token = ''

class Token:
    '''
    Create class for tokens
    2 types of tokens : WEAKNESS and TRAIL
    Within each type there are 3 territory types: FOREST, WATER, MOUNTAIN

    TRAIL
        FOREST 1 2 3 4 5 6
        WATER 1 2 3 4 5 6
        MOUNTAIN 1 2 3 4 5 6

    WEAKNESS
        FOREST I II III IV V VI
        WATER I II III IV V VI
        MOUNTAIN I II III IV V VI
    '''
    def __init__(self, type, territory_type, token_id, is_being_used = False, token_fullname = '' ):
            self.type = type
            self.territory_type = territory_type
            self.is_being_used = False
            self.token_id = token_id 
            self.token_fullname = type + '_' + territory_type + '_' + str(token_id)
            if 'WEAKNESS' in type:
                self.token_img_path = r'assets/images/weaknessTokens/' + type + '_' + territory_type + '_' + str(token_id) + '.jpg'
            else:
                self.token_img_path = r'assets/images/trailTokens/' + type + '_' + territory_type + '_' + str(token_id) + '.png'

    def print_definition(self):
        print(f"Token type: {self.type}")
        print(f"Territory type: {self.territory_type}")
        print(f"token_id: {self.token_id}")
        print(f"Token being used: {self.is_being_used}")
        print(f"Token full name: {self.token_fullname}")
        #print(self.type, self.territory_type, self.token_id, self.is_being_used, self.token_name)

    def __repr__(self):  # Used in lists, debugging, and when you type the object name in the console
        return f"TokenClass(type='{self.type}', territory_type={self.territory_type}, token_id={self.token_id}, is_being_used={self.is_being_used}, token_fullname={self.token_fullname})"

    def __str__(self):  # Used in print() and str() calls
        return f"{self.token_fullname}"

def create_starting_bags_of_tokens(add_skellige: bool):
    '''
    Fill 4 starting lists/bags of tokens
    2 types of tokens : WEAKNESS and TRAIL
    Within each type there are 3 territory types: FOREST, WATER, MOUNTAIN
    '''

    global TRAIL_TOKENS_BAG
    global WEAKNESS_TOKENS_BAG
    global REMOVED_TRAIL_TOKENS_BAG
    global REMOVED_WEAKNESS_TOKENS_BAG

    TRAIL_TOKENS_BAG = []
    WEAKNESS_TOKENS_BAG = []
    REMOVED_TRAIL_TOKENS_BAG = []
    REMOVED_WEAKNESS_TOKENS_BAG = []

    types = ['TRAIL', 'WEAKNESS']
    territory_types = ['FOREST', 'WATER', 'MOUNTAIN']
    tokens_numbers_dict = {
        'TRAIL' : {
              'FOREST':     [6, 7, 8, 10, 16, 17],  #19 Skellige
              'WATER':      [1, 4, 5, 12, 14, 15],  #20 Skellige
              'MOUNTAIN':   [2, 3, 9, 11, 13, 18]   #21 Skellige
        },
        'WEAKNESS' : ['I', 'II', 'III', 'IV', 'V', 'VI']
    }

    if add_skellige == True:
        tokens_numbers_dict['TRAIL']['FOREST'].append(19)
        tokens_numbers_dict['TRAIL']['WATER'].append(20)
        tokens_numbers_dict['TRAIL']['MOUNTAIN'].append(21)

    for token_type,v in tokens_numbers_dict.items():
        if token_type == 'WEAKNESS':
            for territory_type in territory_types:
                for value in v:
                    WEAKNESS_TOKENS_BAG.append( Token( token_type, territory_type, value) )
            
        elif token_type == 'TRAIL':
            for territory_type,value in tokens_numbers_dict[token_type].items():
                for v in value:
                     TRAIL_TOKENS_BAG.append( Token( token_type, territory_type, v) )
    
    random.shuffle(WEAKNESS_TOKENS_BAG)
    random.shuffle(TRAIL_TOKENS_BAG)

    st.toast(":material/token: TOKENS BAGS CREATED :material/token:")
    print("*** TOKENS BAGS CREATED ***")
    return TRAIL_TOKENS_BAG, WEAKNESS_TOKENS_BAG, REMOVED_TRAIL_TOKENS_BAG, REMOVED_WEAKNESS_TOKENS_BAG

def randomly_remove_one_token_from_bag(type: str, territory_type: str):
    if 'WEAKNESS' in type:
        list_to_remove_from = WEAKNESS_TOKENS_BAG
        list_to_add_to = REMOVED_WEAKNESS_TOKENS_BAG
    elif 'TRAIL' in type:
        list_to_remove_from = TRAIL_TOKENS_BAG
        list_to_add_to = REMOVED_TRAIL_TOKENS_BAG

    random.shuffle(list_to_remove_from)

    # iterate through the list of tokens and find the first token that matches the territory type
    for token in list_to_remove_from:
        if token.territory_type == territory_type:
    # remove it from the list and add it to the list of removed tokens
            print("RANDOMLY REMOVED TOKEN: " + token.token_fullname)
            list_to_add_to.append(token)
            list_to_remove_from.remove(token)
            most_recently_chosen_token = token.token_fullname
            return most_recently_chosen_token

def intentionally_remove_one_token_from_bag(type: str, token_fullname: str):

    if isinstance(token_fullname, str) and '_' in token_fullname:
        token_type = token_fullname.split('_')[0]
    else:
        token_type = token_fullname.type
        token_fullname = token_fullname.token_fullname

    if 'WEAKNESS' in type:
        list_to_remove_from = WEAKNESS_TOKENS_BAG
        list_to_add_to = REMOVED_WEAKNESS_TOKENS_BAG
    elif 'TRAIL' in type:
        list_to_remove_from = TRAIL_TOKENS_BAG
        list_to_add_to = REMOVED_TRAIL_TOKENS_BAG

    for token in list_to_remove_from:
        if token.token_fullname == token_fullname:
            print("INTENTIONALLY REMOVED TOKEN: " + token.token_fullname)
            list_to_add_to.append(token)
            list_to_remove_from.remove(token)
            most_recently_chosen_token = token.token_fullname
            return most_recently_chosen_token
    
    print(f"Failed to find and remove given token: {token_fullname}")

def return_token_to_bag(token_name: str):
    
    if isinstance(token_name, str) and '_' in token_name:
        token_type = token_name.split('_')[0]
    else:
        token_type = token_name.type
        token_name = token_name.token_fullname

    if token_type == 'WEAKNESS':
        list_to_remove_from = REMOVED_WEAKNESS_TOKENS_BAG
        list_to_add_to = WEAKNESS_TOKENS_BAG
    elif token_type == 'TRAIL':
        list_to_remove_from = REMOVED_TRAIL_TOKENS_BAG
        list_to_add_to = TRAIL_TOKENS_BAG

    for token in list_to_remove_from:
        if token.token_fullname == token_name:
            print(f"{token_type} TOKEN RETURNED TO CORRESPONDING BAG: " + token.token_fullname)
            list_to_add_to.append(token)
            list_to_remove_from.remove(token)
            return
    
    print(f"Failed to return given token: {token_name}")

def get_color_for_token(token_name: str) -> str:
    if isinstance(token_name, str):
        pass
    elif token_name is None:
        return
    else:
        token_name = token_name.token_fullname

    if 'FOREST' in token_name:
        return 'green'
    if 'WATER' in token_name:
        return 'blue'
    if 'MOUNTAIN' in token_name:
        return 'grey'
    
# MAIN
# create_starting_bags_of_tokens()
# print(WEAKNESS_TOKENS_BAG)
# print(TRAIL_TOKENS_BAG)