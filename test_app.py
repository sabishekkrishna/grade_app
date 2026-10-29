from app import total, average

def test_total():
    assert total(92,95,87,90) == 364

def test_average():
    assert average(92,95,87,90) == 91