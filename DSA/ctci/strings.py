"""
CTCI String / Array Problems
"""


"""
1. Is Unique?
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

Input - "ABCDEFG"
Output - True

Input - "ABCAEDFT"
Output - False - "A" is repeated twice

Questions to ask -
1. Do we care about case sensitivity?
2. Are we allowed to modify the original input?

Solution - 
    If we're allowed to use an additional data structure - this problem becomes trivial. We can use a set.
    If we cannot use an additional data structure - a brute force method would be to use a nested for loop checking all letters for each letter, if we come across the same letter - return false because that's a duplicate
        The run time of this would be O(n^2)
    Another method would be to first sort the string, then using a loop checking the current index and the one to the right of it - if there the same then we have duplicates - return false
        The run time of this would be O(n log n) - using "sort" in python is (n log n)
"""

def is_unique_set(input):
    modified_input = set(input)
    if len(input) != len(modified_input):
        return False
    return True

def is_unique(input):
    modified_input = sorted(input)
    for char in range(len(modified_input) - 1):
        if modified_input[char] == modified_input[char + 1]:
            return False
    return True


"""
2. Check Permutation?
Given two strings, write a method to decide if one is a permutation of the other.
A permutation of a string means that both the strings contain the same characters, but the order might be different.
Input - "ABC" & "CBA"
Output - True

Input - "ABC" & "DEG" 
Output - False

Questions to ask -
1. Does case sensitivity matter?

Solution -
    If case sensitivity does not matter, one way to solve this is to use sorting.
    If we sort both the strings, then we should be able to loop through the whole string and each character
        that we loop through should be equal to each other.
        If we come across any characters that are different, then we know it's not a permutation
    The downside to using sorting is that python's "sorted()" is using the timsort (n log n)
        This means that the runtime for the first implementation is (n log n)
   

    What if we can't use sorting?
        If we can't use sorting, we can use dictionaries.
        Iterate through both strings, adding the count of each letter to each respective dictionary.
        Then we can see if both dictionaries are equal to each other
"""

def is_permutation_sorting(x, y):
    if len(x) != len(y):
        return False
    x = sorted(x)
    y = sorted(y)
    for i in range(len(x)): 
        if x[i] != y[i]:
            return False
    return True

def is_permutation_dictionaries(x,y):
    if len(x) != len(y):
        return False
    x_dict = {}
    y_dict = {}
    for char in x:
        if char not in x_dict:
            x_dict[char] = 1
        else:
            x_dict[char] += 1

    for char in y:
        if char not in y_dict:
            y_dict[char] = 1
        else:
            y_dict[char] += 1

    if x_dict != y_dict:
        return False
    return True


"""
3. URLify
Write a method to replace all spaces in a string with '%20'. You may assume that the
string has sufficient space at the end to hold the additional characters. You're also given
the true length of the string

Input - "Mr John Smith    ", 13
Output - "Mr%20%John%20Smith"

Solution -
    Part of the initial issue is that we don't know when the string is suppose to end
    We can't loop through the entire string and replace the spaces with "%20" because when we reach the end
    we'll end up with multiple "%20%20%20"

    What if we split the string on spaces, and then for each item in the array add "%20" in between
    the items
        So essentially we would have:
            -> ["Mr", "John", "Smith"]
            -> new_str = "Mr%20John%20Smith"
"""

def urlify(x):
    my_list = x.split()
    result = ""
    for word in range(len(my_list)):
        # checking if last word
        if my_list[word] == my_list[-1]:
            result += my_list[word]
        else:
            result += my_list[word] + "%20"
    return result
