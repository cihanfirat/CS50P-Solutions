from bank import value

def test_incorrect_values():
    assert value("1234")==100
def test_case_insensivity():
    assert value("HELLO")==0
def test_entire_phrase():
    assert value("hello cihan")==0
