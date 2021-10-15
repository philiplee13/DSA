"""
Working through Chapter 1 - Arrays and Strings
"""

"""
1.1 Is Unique? -> Implement an algorithim to determine if a string has all unqiue characters?
Follow up question -> What if we cannot use any additional data structures?

Input:
    ABCDEFA
Output:
    False

Initial thought here is to use a set - this takes care of the duplicate characters.
Follow up - we can first sort the string - then loop through checking the current letter and the letter next to it
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

Input:
    ABCD, DACB
Output:
    True

Permutations - a string that is a rearrangment of the letters
We can use a dictionary here for each string, if the two dictionaries are equal to each other - the strings are permutations of each other
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

Input:
    Testing for Mr John Smith  ,
Output:
    this should return Mr%20John%20Smith%20%20

Initial Thought - loop through the string looking for any white space - if so replace it with the "%20", if not add the letter of the current iteration
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


"""
1.4 Palindrome Permutation -> Given a string, write a function to check if it's a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards
    Ex - "racecar" -> the same forwards and backwards
A permutation is a rearrangement of letters.
    Ex - "code" -> "odce", "dceo"

Input:
    Tact Coa
Output:
    True (taco cat, atco cta)

Let's break this problem up into two portions.
    1st - Palindrome portion
        Because it has to be a palindrome, we know that the string must have "matching" chars, and at most only one char can have an odd count
    2nd - Permutation
        A permutation is just a rearrangement of letters - if we know a string is a palindrome -> we already know it's a permutation
        This is because the string backwards is a "rearrangement" of the letters
    So then - we can use a dictionary to loop through the string and count the occurences of each "char"
    After that - we can loop through the dictionary to see if there is more than one char that has only one occurence - if there's more than one
    char that has one occurence - return False - not a palindrome
    -> If there is only one char that has one occurence - return True
"""
def palindrome_permutation(string):
    # string processing - lowercase and remove whitespace
    string = string.lower()
    string = string.replace(" ", "")

    d = {}
    count = 0

    # fill up the dictionary
    for letter in string:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
    # loop through the dictionary - and increment count if our value is 1
    for k, v in d.items():
        if v == 1:
            count += 1
    return count <= 1


"""
1.5 One Away
There's 3 types of edits we can make to a string, insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one or zero edits away

pale, ple -> True
pales, pale -> True
pale, bake -> False
"""

def one_away(str_1, str_2):
    # case of both strings being equal to each other
    if str_1 == str_2:
        return True
    # case of if the difference between strings are greater than 1
    if abs(len(str_1) - len(str_2)) > 1:
        return False
    count = 0
    longer_lst = None
    shorter_lst = None
    # determine which array is longer - use the longer one in for loop
    if len(str_1) > len(str_2):
        longer_lst = list(str_1)
        shorter_lst = list(str_2)
    else:
        longer_lst = list(str_2)
        shorter_lst = list(str_1)
    # for loop to determine if each letter is in the other array
    for letter in range(len(longer_lst)):
        if longer_lst[letter] not in shorter_lst:
            count += 1
    # if the count is greater than or equal 2 - that means it's more than one edit away
    if count >= 2:
        return False
    return True




if __name__ == "__main__":
    print(one_away("pale","ple"))
    print(one_away("pale","pales"))
    print(one_away("pale","bake"))
    print(one_away("pales","palessss"))