from app.calc_bonus import calculate_bonuses


def test_calculate_bonuses():
    result = calculate_bonuses(900)

    assert 0 == result

