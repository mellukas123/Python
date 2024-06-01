import play_with_wording

def test_swap_case():
    text = "QWE qwe asd I"
    assert play_with_wording.swap_case(text) == "qwe QWE ASD i"


def test_shortest_word(text):
    assert play_with_wording.shortest_word(text) == "I"
