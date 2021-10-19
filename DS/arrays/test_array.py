import arrays as arr

"""
Testing for Array Question 1.1
"""

def test_is_unique1():
    print("Testing for ABCDEFA, should return False")
    assert arr.is_unique("ABCDEFA") == False

def test_is_unique2():
    print("Testing for ABCDEFG, should return True")
    assert arr.is_unique("ABCDEFG") == True

def test_is_unique_follow_up_implementation1():
    print("Testing for ABCDEFA, should return False")
    assert arr.is_unique("ABCDEFA") == False

def test_is_unique_follow_up_implementation2():
    print("Testing for ABCDEFG, should return True")
    assert arr.is_unique("ABCDEFG") == True

"""
Testing for Array Question 1.2
"""

def test_check_permutation1():
    print("Testing for ABCD & DACB, this should return True")
    assert arr.check_permutation("ABCD", "DACB") == True

def test_check_permutation2():
    print("Testing for ABCDE & DACB, this should return False")
    assert arr.check_permutation("ABCDE", "DACB") == False

"""
Testing for Array Question 1.3
"""

def test_urlify1():
    print("Testing for Mr John Smith  , this should return Mr%20John%20Smith%20%20")
    assert arr.urlify("Mr John Smith  ") == "Mr%20John%20Smith%20%20"

def test_urlify2():
    print("Testing for   Mr John Smith, this should return %20%20Mr%20John%20Smith")
    assert arr.urlify("  Mr John Smith") == "%20%20Mr%20John%20Smith"

"""
Testing for Array Question 1.4
"""

def test_palindrome_permutation1():
    print("Testing for palindrom permutation, Tact Coa - should return True")
    assert arr.palindrome_permutation("Tact Coa") == True

def test_palindrome_permutation2():
    print("Testing for palindrom permutation, Code - should return False")
    assert arr.palindrome_permutation("Code") == False


"""
Testing for Array Question 1.5
"""

def test_one_away1():
    print("Testing for One Away, pale and pales - should return True")
    assert arr.one_away("pale","pales") == True

def test_one_away2():
    print("Testing for One Away, pale and ple - should return True")
    assert arr.one_away("pale","ple") == True

def test_one_away3():
    print("Testing for One Away, pale and bake - should return False")
    assert arr.one_away("pale","bake") == False

def test_one_away4():
    print("Testing for One Away, pale and palessss - should return False")
    assert arr.one_away("pale","palessss") == False

"""
Testing for Array Question 1.6
"""

def test_string_compression1():
    print("Testing for String Compression, aabcccccaaa should return a2b1c5a3")
    assert arr.string_compression("aabcccccaaa") == "a2b1c5a3"

def test_string_compression2():
    print("Testing for string compression, abc -> abc")
    assert arr.string_compression("abc") == "abc"

