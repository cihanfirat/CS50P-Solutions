from twttr import shorten

def test_lower():
    assert shorten("cihan")=="chn"
def test_upper():
    assert shorten("CIHAN")=="CHN"
def test_number():
    assert shorten("1234")=="1234"
def test_punctuation():
    assert shorten("!,.:;?")=="!,.:;?"
