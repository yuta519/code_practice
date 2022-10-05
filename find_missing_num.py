# You are given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x. You have to find x. The input array is not sorted. Look at the below array and give it a try before checking the solution.


def find_missing_num(input_array: list[int]):
    n: int = len(input_array) + 1
    assumed_sum: int = sum([i for i in range(1, n + 1)])
    input_sum: int = sum(input_array)
    return assumed_sum - input_sum


print(find_missing_num([1]))
print(find_missing_num([3, 7, 1, 2, 8, 4, 5]))
print(find_missing_num([9,6,4,2,3,5,7,1]))
