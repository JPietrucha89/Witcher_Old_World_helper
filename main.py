import tokens
import random

global TRAIL_TOKENS_BAG
global WEAKNESS_TOKENS_BAG

if __name__ == "__main__":

    tokens.create_starting_bags_of_tokens() # at this moment there should be 2 lists of tokens: 18 WEAKNESS tokens in WEAKNESS_TOKENS_BAG and 18 tokens in TRAIL_TOKENS_BAG, both bags are already randomized/shuffled

    # print(tokens.WEAKNESS_TOKENS_BAG)
    # print(tokens.TRAIL_TOKENS_BAG)

    for weakness_token in tokens.WEAKNESS_TOKENS_BAG:
        #weakness_token.print_definition()
        print(weakness_token.token_fullname)
    
    for trail_token in tokens.TRAIL_TOKENS_BAG:
        #trail_token.print_definition()
        print(trail_token.token_fullname)

# manually get one token for FOREST, WATER, MOUNTAIN to place initial monsters
# remove those tokens from the TRAIL_TOKENS_BAG
    tokens.intentionally_remove_one_token_from_bag('WEAKNESS', 'MOUNTAIN', 'WEAKNESS_MOUNTAIN_I')

    tokens.intentionally_remove_one_token_from_bag('TRAIL', 'FOREST', 'TRAIL_FOREST_X')
    tokens.intentionally_remove_one_token_from_bag('TRAIL', 'WATER', 'TRAIL_WATER_X')
    tokens.intentionally_remove_one_token_from_bag('TRAIL', 'MOUNTAIN', 'TRAIL_MOUNTAIN_X')

    quit()

# debug
    token = tokens.Token('TRAIL', 'WATER', 1)
    token.print_definition()
    