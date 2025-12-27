from plates import is_valid

def test_begin_alphabetic():
    assert is_valid("11111")==False
def test_lenght():
    assert is_valid("A")==False
def test_middle_number():
    assert is_valid("AAA22A")==False
def test_zero():
    assert is_valid("AAA022")==False
def test_alphanumeric():
    assert is_valid("AA!22")==False
