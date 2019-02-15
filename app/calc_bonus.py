def calculate_bonuses (the_sum_of_current_purchase):
    """
        calculate_bonuses(900)
        0...
        calculate_bonuses(1_000)
        50...
        calculate_bonuses(16_000)
        1120...
        calculate_bonuses(150_000)
        15000...
    """
    the_sum_of_previous_purchases = 0
    blue_card_percent = 0.05
    silver_card_percent = 0.07
    gold_card_percent = 0.1
    the_sum_of_previous_purchases = the_sum_of_previous_purchases + the_sum_of_current_purchase

    if the_sum_of_previous_purchases <1000:
        bonus_for_purchase = 0
    if 1000 <= the_sum_of_previous_purchases <= 15_000:
        bonus_for_purchase = the_sum_of_current_purchase * blue_card_percent

    if 15001 <= the_sum_of_previous_purchases < 150_000:
        bonus_for_purchase = the_sum_of_current_purchase * silver_card_percent

    if the_sum_of_previous_purchases >= 150_000:
        bonus_for_purchase = the_sum_of_current_purchase * gold_card_percent

    return bonus_for_purchase

print(calculate_bonuses(150_000))
print(calculate_bonuses(15_000))
print(calculate_bonuses(1000))
print(calculate_bonuses(900))

