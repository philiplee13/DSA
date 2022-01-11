# run these tests with the command pytest DSA/ctci/tests/test_strings.py 
# this is assuming your in the root dir

from DSA.ctci import strings
"""
1. Is Unique
"""
def test_is_unique_set_true():
    assert strings.is_unique_set("ABCDE") == True

def test_is_unique_set_false():
    assert strings.is_unique_set("ABCDEE") == False


def test_is_unique_true():
    assert strings.is_unique("ABCDE") == True


def test_is_unique_false():
    assert strings.is_unique("ABCDEE") == False

"""
2. Check Permutation
"""
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

"""
3. URLify
"""
def test_urlify():
    assert strings.urlify("Mr John Smith    ") == "Mr%20John%20Smith"

"""
4. Palindrome Permutation
"""
def test_palindrome_permutation_true():
    assert strings.palindrome_permutation("taco cat") == True
    # taco cat
    # taco cat

def test_palindrome_permutation_false():
    assert strings.palindrome_permutation("civil") == False
    # civil
    # livic

def test_palindrome_permutation_true_second_test():
    assert strings.palindrome_permutation("civic") == True
    # civic
    # civic

def test_palindrome_permutation_false_second_test():
    assert strings.palindrome_permutation("livci") == False
    # livci
    # icvil

def test_palindrome_permutation_ctci_true():
    assert strings.palindrome_permutation_ctci("taco cat") == True

def test_palindrome_permutation_ctci_false():
    assert strings.palindrome_permutation_ctci("civil") == False

def test_palindrome_permutation_ctci_true_second_test():
    assert strings.palindrome_permutation_ctci("civic") == True

def test_palindrome_permutation_ctci_false_second_test():
    assert strings.palindrome_permutation("livci") == False

"""
5. One Away
"""

def test_one_away_true():
    assert strings.one_away("pale", "ple") == True

def test_one_away_false():
    assert strings.one_away("pale", "bake") == False

def test_one_away_second_true():
    assert strings.one_away("pales", "pale") == True

def test_one_away_second_false():
    assert strings.one_away("pales", "ple") == False


"""
6. String Compression
"""
def test_string_compression_true():
    assert strings.string_compression("aabcccccaaa") == "a2b1c5a3"

def test_strings_compression_true_second_test():
    assert strings.string_compression("abbbbddde") == "a1b4d3e1"