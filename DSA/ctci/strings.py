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

"""
4. Palindrome Permutation
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. The palindrome does not need to be limited to just
dictionary words.
You can ignore casing and non-letter characters.

Input - "Tact Coa"
Output - True
    permuatations - "Taco cat", "atco cta", etc.

Solution - 
    The key for this problem is to determine whether or not the string is a palindrome
    The permutation is just a rearrangement of the letters, so all we need to do is make sure
    that we keep the original letters.


    My Original Solution (Not sure if this is correct)
    For a palindrome - we might be able to use two pointers, one at the start of the string
    and the other at the end.
        We can then iterate through the string and move towards the center
        checking if the pointers are equal to each other. If they are, move onto the next letters
        If they aren't - this isn't a palindrome

        Example - "taco cat":
            the first letter and last letter is t - this passes
            the second letter and second to last letter is a -  this passes
            next letter is both c - this passes
            the next letter is a "o" and a "space" - so we need to handle this edge case
                can we check if it's a space - either inc / dec the letter that you're on?
            so in this case - we have "o" and a "space" - we would dec the 2nd pointer to then point to
            the next letter, in this case "o"

    CTCI Solution
        Their solution is more elegant - the logic here is to think about what we need
        to be able to write a string the same way backwards and forwards.
        We need the same set of letters - on both sides (imagine we cut the string in half)
        Only the middle character can be odd
        So we can use a dictionary here, and make sure that only one letter has a count greater than 1
"""
def palindrome_permutation(x):
    first = 0
    last = len(x) - 1
    print(last)
    while first < last:
        print(f"first index and last index is {first} and {last}")
        print(f"first and last letters are {x[first]} and {x[last]}")
        if x[first] == " ":
            print(f"first letter was a space {x[first]}")
            first += 1
        elif x[last] == " ":
            print(f"last letter was a space {x[last]}")
            last -= 1
        if x[first] != x[last]:
            return False
        print(f"first and last letter matches {x[first]} and {x[last]}")
        first += 1
        last -= 1
    return True

def palindrome_permutation_ctci(x):
    d = {}
    count = 0
    for i in range(len(x)):
        # if space - do nothing
        if x[i] == " ":
            continue
        if x[i] not in d:
            d[x[i]] = 1
        else:
            d[x[i]] += 1
    for k, v in d.items():
        print(f"k is {k} v is {v}")
        if v == 1:
            count += 1
    if count > 1:
        return False
    return True