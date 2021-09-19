"""
Given an array of nums [-1,2,3,1,-3,2]
Find the max sum of a subarray with max length of 2
"""

"""
Brute force method here is to loop through the array and store the results in the an external data structure
But if our input size is really large - space being O(n) will be costly.
It's better just to compare each value and only hold the "max"
"""
def max_sum(arr):
    curr_max = nums[0]
    for i in range(len(nums) - 1):
        curr = nums[i] + nums[i+1]
        if curr > curr_max:
            curr_max = curr
    return curr_max

def min_sum(arr):
    curr_min = nums[0]
    for i in range(len(nums) - 1):
        curr = nums[i] + nums[i + 1]
        if curr < curr_min:
            curr_min = curr
    return curr_min


"""
Now take an array and find all subarrays that equal to a certain value.
This problem is different from before - this window is dynamically sizing.
The method is still the same - but when we calculate the new "sum" we need to take into consideration if it's bigger or smaller than our target value
If it's bigger -> shrink the window
If it's smaller -> expand the window.
"""

if __name__== "__main__":
    nums = [-1,2,3,1,-3,2]
    print(max_sum(nums))
    print(min_sum(nums))