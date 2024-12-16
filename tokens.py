import random

'''
Create class for tokens
2 types of tokens : WEAKNESS and TRAIL
Within each type 3 territory types: FOREST, WATER, MOUNTAIN

TRAIL
    FOREST 1 2 3 4 5 6
    WATER 1 2 3 4 5 6
    MOUNTAIN 1 2 3 4 5 6

WEAKNESS
    FOREST I II III IV V VI
    WATER I II III IV V VI
    MOUNTAIN I II III IV V VI

'''

global TRAIL_TOKENS_BAG
global WEAKNESS_TOKENS_BAG

TRAIL_TOKENS_BAG = []
WEAKNESS_TOKENS_BAG = []

class Token:
    def __init__(self, type, territory_type, token_id, is_being_used = False, token_fullname = '' ):
            self.type = type
            self.territory_type = territory_type
            self.is_being_used = False
            self.token_id = token_id 
            self.token_fullname = type + '_' + territory_type + '_' + str(token_id)

    def print_definition(self):
        print(f"Token type: {self.type}")
        print(f"Territory type: {self.territory_type}")
        print(f"token_id: {self.token_id}")
        print(f"Token being used: {self.is_being_used}")
        print(f"Token full name: {self.token_fullname}")
        #print(self.type, self.territory_type, self.token_id, self.is_being_used, self.token_name)

class Bag_of_tokens:
     def __init__(self, type):
          pass
     

def create_starting_bags_of_tokens():
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

    for token_type,v in tokens_numbers_dict.items():
        if token_type == 'WEAKNESS':
            for territory_type in territory_types:
                for value in v:
                    #print(token_type, territory_type, value)
                    WEAKNESS_TOKENS_BAG.append( Token( token_type, territory_type, value) )
            
        elif token_type == 'TRAIL':
            for territory_type,value in tokens_numbers_dict[token_type].items():
                #print(token_type,v)
                #print(territory_type,value)
                for v in value:
                     #print(token_type, territory_type, v)
                     TRAIL_TOKENS_BAG.append( Token( token_type, territory_type, v) )
    
    random.shuffle(WEAKNESS_TOKENS_BAG)
    random.shuffle(TRAIL_TOKENS_BAG)
    # print(WEAKNESS_TOKENS_BAG)
    # print(TRAIL_TOKENS_BAG)


def randomly_remove_one_token_from_bag(type, territory_type):
     pass

def intentionally_remove_one_token_from_bag(type, territory_type, token_fullname):
    if type == 'WEAKNESS':
        list_to_search = WEAKNESS_TOKENS_BAG
    elif type == 'TRAIL':
        list_to_search = TRAIL_TOKENS_BAG

    list_to_search.remove()

def return_token_to_bag(token_name):
    if type == 'WEAKNESS':
        list_to_add = WEAKNESS_TOKENS_BAG
    elif type == 'TRAIL':
        list_to_add = TRAIL_TOKENS_BAG

# MAIN
# create_starting_bags_of_tokens()
# print(WEAKNESS_TOKENS_BAG)
# print(TRAIL_TOKENS_BAG)