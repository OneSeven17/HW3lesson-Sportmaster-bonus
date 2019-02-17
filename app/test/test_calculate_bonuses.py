from app.calc_bonus import calculate_bonuses


def test_calculate_bonuses():
    result = calculate_bonuses(1_000)

    assert 50 == result

def test_bonus_over_limit()
    result = calculate_bonuses(1_000_000)