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





