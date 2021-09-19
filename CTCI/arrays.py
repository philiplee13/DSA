"""
Working through Chapter 1 - Arrays and Strings
"""

"""
1.1 Is Unique? -> Implement an algorithim to determine if a string has all unqiue characters?
Follow up question -> What if we cannot use any additional data structures?
"""

def is_unique(string):
    s = set()
    for char in string:
        if char not in s:
            s.add(char)
        else:
            return False
    return True

# Follow up question implementation
def is_unique_no_additional_structures(string):
    sorted_str = sorted(string)
    print(sorted_str)
    for i in range(0,len(sorted_str) - 1):
        if sorted_str[i] == sorted_str[i+1]:
            return False
    return True

# for "range()" in python, there's 3 arguements
# range (start, stop, step)
# the start and step is optional
# the "stop" is required, so doing range(len(sorted_str), len(sorted_str) - 1) essentially tells us to "skip" over the loop
# in the example "ABCDEFA" -> if we do range(len(sorted_str), len(sorted_str)) -> this translates to (range(7, 6)) -> which is false -> skips loop


"""
1.2 Check Permutation -> Given two strings, write a method to decide if one is a permutation of the other
"""
def check_permutation(first_str, second_str):
    d1 = {}
    d2 = {}
    for char in first_str:
        if char not in d1:
            d1[char] = 1
        else:
            d1[char] += 1
    for char in second_str:
        if char not in d2:
            d2[char] = 1
        else:
            d2[char] += 1
    return d1 == d2

"""
1.3 URLify -> Given a string, replace all spaces with "%20"
"""

# if we can use built in methods - just use replace, I'll assume we can't for this one
def urlify(string):
    new_str = ""
    for char in range(len(string)):
        if string[char] == " ":
            new_str += "%20"
        else:
            new_str += string[char]
    return new_str




if __name__ == "__main__":
    # print("Array Question 1.1")
    # print("Is Unique? -> Implement an algorithim to determine if a string has all unqiue characters?")
    # print("Testing for ABCDEFA, this should return False")
    # print(is_unique("ABCDEFA"))
    # print("\n")
    # print("Testing for ABCDEFG, this should return True")
    # print(is_unique("ABCDEFG"))
    # print("\n")
    # print("Testing for ABCDEFA (Follow up Implementation), this should return False")
    # print(is_unique_no_additional_structures("ABCDEFA"))
    # print('\n')
    # print("Testing for ABCDEFG (Follow up Implementation), this should return True")
    # print(is_unique_no_additional_structures("ABCDEFG"))
    # print('\n')
    # print("Array Question 1.2")
    # print("Check Permutation -> Given two strings, write a method to decide if one is a permutation of the other")
    # print("Testing for ABCD & DACB, this should return true")
    # print(check_permutation("ABCD", "DACB"))
    # print("\n")
    # print("Testing for ABCDE & DACB, this should return False")
    # print(check_permutation("ABCDE", "DACB"))
    # print("\n")
    # print("Array Question 1.3")
    # print("URLify -> Given a string, replace all spaces with %20")
    # print("Testing for Mr John Smith  , this should return Mr%20John%20Smith%20%20")
    print(urlify("Mr John Smith  "))