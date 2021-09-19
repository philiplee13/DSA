from arrays import *

"""
Testing for Array Question 1.1
"""

def test_is_unique1():
    print("Testing for ABCDEFA, should return False")
    assert is_unique("ABCDEFA") == False

def test_is_unique2():
    print("Testing for ABCDEFG, should return True")
    assert is_unique("ABCDEFG") == True

def test_is_unique_follow_up_implementation1():
    print("Testing for ABCDEFA, should return False")
    assert is_unique("ABCDEFA") == False

def test_is_unique_follow_up_implementation2():
    print("Testing for ABCDEFG, should return True")
    assert is_unique("ABCDEFG") == True

"""
Testing for Array Question 1.2
"""

def test_check_permutation1():
    print("Testing for ABCD & DACB, this should return True")
    assert check_permutation("ABCD", "DACB") == True

def test_check_permutation2():
    print("Testing for ABCDE & DACB, this should return False")
    assert check_permutation("ABCDE", "DACB") == False

"""
Testing for Array Question 1.3
"""

def test_urlify1():
    print("Testing for Mr John Smith  , this should return Mr%20John%20Smith%20%20")
    assert urlify("Mr John Smith  ") == "Mr%20John%20Smith%20%20"

def test_urlify2():
    print("Testing for   Mr John Smith, this should return %20%20Mr%20John%20Smith")
    assert urlify("  Mr John Smith") == "%20%20Mr%20John%20Smith"

"""

"""