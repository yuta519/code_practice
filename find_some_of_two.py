"""
Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value. Return true if the sum exists and return false if it does not. Consider this array and the target sums:
"""

def find_some_of_two(array: list[int], value: int) -> bool:
    for target in array:
        if value - target in array and value - target != target:
            return True
    return False


print([find_some_of_two([5, 7, 1, 2, 8, 4, 3], i) for i in[3, 20, 1, 2, 7]])
