from  count_words import CountWords
    
def test_two_words_ending_with_s():
    words = CountWords().count("dogs cats")
    assert words == 2
    
def test_two_words_ending_with_r():
    words = CountWords().count("door car")
    assert words == 2
    
def test_no_words_at_all():
    words = CountWords().count("dog cat")
    assert words == 0
    
def test_no_words_at_all_more():
    words = CountWords().count("dog cat sun dog cat sun dog cat sun dog cat sun dog cat sun dog cat sun dog cat sun dog cat sun dog cat sun dog cat sun")
    assert words == 0

def test_intermediate_characters_no_alpha():
    words = CountWords().count("do.gs ca.ts")
    assert words == 2
    
def test_two_words_ending_with_S():
    words = CountWords().count("DOGS CATS")
    assert words == 2
    
def test_two_words_ending_with_R():
    words = CountWords().count("DOOR CAR")
    assert words == 2
    
def test_two_words_ending_with_s_and_R():
    words = CountWords().count("DOgs CAR")
    assert words == 2
    
def test_two_words_ending_with_multiple_r_and_s():
    words = CountWords().count("DOgs . . CaR-cats")
    assert words == 3
    
def test_mixed_endings():
    words = CountWords().count("car cats")
    assert words == 2
    
def test_only_non_alpha():
    words = CountWords().count("!!!")
    assert words == 0