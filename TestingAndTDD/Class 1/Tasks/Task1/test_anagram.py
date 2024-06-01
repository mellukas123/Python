import anagram

def test_is_anagrams():
    anagrams = "ABC"
    assert anagram.is_anagrams('ABC', 'CBA') == True

