from DSA.ctci import strings

def test_is_unique_set_true():
    assert strings.is_unique_set("ABCDE") == True

def test_is_unique_set_false():
    assert strings.is_unique_set("ABCDEE") == False


def test_is_unique_true():
    assert strings.is_unique("ABCDE") == True


def test_is_unique_false():
    assert strings.is_unique("ABCDEE") == False

def test_is_permutation_true():
    assert strings.is_permutation_sorting("ABC","CBA") == True

def test_is_permutation_false():
    assert strings.is_permutation_sorting("ABC","DEF") == False

def test_is_permutation_dictionary_true():
    assert strings.is_permutation_dictionaries("ABC","CBA") == True

def test_is_permutation_dictionary_false():
    assert strings.is_permutation_dictionaries("ABC", "DEF") == False

def test_is_permutation_length():
    assert strings.is_permutation_dictionaries("ABC", "DEFFF") == False



if __name__ == "__main__":
    test_is_unique_set_true()
    test_is_unique_set_true()
    test_is_unique_true()
    test_is_unique_false()
    test_is_permutation_true()
    test_is_permutation_false()
    test_is_permutation_dictionary_true()
    test_is_permutation_dictionary_false()
    test_is_permutation_length()
    print("All tests have passed")