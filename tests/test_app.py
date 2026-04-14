from app import calculate_area

def test_area():
    assert calculate_area(5) == 78.53981633974483

def test_negative_radius():
    assert calculate_area(-1) == "Invalid"
