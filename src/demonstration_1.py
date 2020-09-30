"""
Given a list of integers and a target value, return the indices of the two numbers in the list that add up to a specific target.

*Note: You can assume that each input has exactly one solution, and the same element cannot be used more than once.*

Example:

Given nums = [3, 8, 12, 17], target = 15,

Because nums[0] + nums[2] = 3 + 12 = 15,
return [0, 2].
"""
# Understand: 
# The integers in the array will be summed - iterate through in a for loop? use range? 
# IF their sum is equivalent to 15
# Return the INDEX (not the numbers) where the integers that equate to 15 


#Class: 
#Use a dictionary to give the numbers an index number. 
#SUBTRACT 15 from the index value, see if the value to sum it back to 15 is in the dictionary.
#

def two_sum(nums, target):
    map = {element: index for index, element in enumerate(nums)}

    for i in range(len(nums)):
        diff = target - nums[i]
        #check if diff is a key in our map (dictionary)
        if diff in map:
            return [i, map[diff]]
    # if we get here we didn't find two elements that equal 15.
    return "No two elements sum to the target value"

nums = [3, 8, 12, 17]
target = 15
print(two_sum(nums, target))
