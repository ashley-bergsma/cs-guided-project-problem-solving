"""
Given an integer value `n`, write a function that will return a list of the string representation of numbers from 1 to `n`.

However, there are a few additional rules to follow:

- For multiples of three, it should output "Lambda" instead of the number.
- For multiples of five, it should output "School" instead of the number.
- For numbers which are multiples of three and five, it should output "LambdaSchool" instead of the number.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Lambda",
    "4",
    "School",
    "Lambda",
    "7",
    "8",
    "Lambda",
    "School",
    "11",
    "Lambda",
    "13",
    "14",
    "LambdaSchool"
]
"""

# The number is passed as an argument - not a list 
# The return will be an array that is as many elements long as the number argument passed 
# If the number at that index is divisible by 5 or 3 or 15 - a special message will be returned rather than the number value


def lambda_school(n):
    # initialize a return array 
    return_array = []

    # declare a for loop to iterate over numbers 1 (we are not starting at 0) through the given number argument + 1 - to account for range exclusivity 
    for number in range(1, n + 1): 
    # define the conditions to make them readable in the IF clauses
        div_by_3 = (number % 3 == 0)
        div_by_5 = (number % 5 == 0)

    # start with the most restritive clause first, because 15 and 30 and other numbers will be divisible by 3 AND 5
        if div_by_3 and div_by_5:
            return_array.append("LambdaSchool")
        elif div_by_3:
            return_array.append("Lambda")
        elif div_by_5: 
            return_array.append("School")
        else:
            return_array.append(number)
    return return_array

print(lambda_school(15))
print(lambda_school(30))

