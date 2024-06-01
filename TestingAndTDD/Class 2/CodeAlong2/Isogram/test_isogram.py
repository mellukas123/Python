# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.
#
# Example: (Input --> Output)
#
# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)
#
# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false
import isogramm
def test_is_isogram():
    assert isogramm.is_isogram("Dermatoglyphics") == True
    assert isogramm.is_isogram("isogram") == True
    assert isogramm.is_isogram("aba") == False
    assert isogramm.is_isogram("moOse") == False
    assert isogramm.is_isogram("isIsogram") == False
    assert isogramm.is_isogram("") == True
