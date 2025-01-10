import pytest
from tokens import create_starting_bags_of_tokens
from tokens import randomly_remove_one_token_from_bag

def test_bags_of_tokens():
    TRAIL_TOKENS_BAG, WEAKNESS_TOKENS_BAG, REMOVED_TRAIL_TOKENS_BAG, REMOVED_WEAKNESS_TOKENS_BAG = create_starting_bags_of_tokens()
    assert len(TRAIL_TOKENS_BAG) == 18
    assert len(WEAKNESS_TOKENS_BAG) == 18
    assert len(REMOVED_TRAIL_TOKENS_BAG) == 0
    assert len(REMOVED_WEAKNESS_TOKENS_BAG) == 0

    # for territory_type in ['FOREST', 'WATER', 'MOUNTAIN']:
    #     for y in range(6):
    #         randomly_remove_one_token_from_bag('TRAIL', territory_type)
    #         randomly_remove_one_token_from_bag('WEAKNESS', territory_type)

    # assert len(TRAIL_TOKENS_BAG) == 0
    # assert len(WEAKNESS_TOKENS_BAG) == 0
    # assert len(REMOVED_TRAIL_TOKENS_BAG) == 18
    # assert len(REMOVED_WEAKNESS_TOKENS_BAG) == 18