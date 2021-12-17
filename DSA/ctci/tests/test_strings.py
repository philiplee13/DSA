from DSA.ctci import strings

def test_is_unique_set_true():
    assert strings.is_unique_set("ABCDE") == True

def test_is_unique_set_false():
    assert strings.is_unique_set("ABCDEE") == False


def test_is_unique_true():
    assert strings.is_unique("ABCDE") == True


def test_is_unique_false():
    assert strings.is_unique("ABCDEE") == False



if __name__ == "__main__":
    test_is_unique_set_true()
    test_is_unique_set_true()
    test_is_unique_true()
    test_is_unique_false()
    print("All tests have passed")