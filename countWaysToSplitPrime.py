"""
count the number of ways the string can split to get pime number

Given a string of length n consisting of digits [0-9], count the number of ways the given string can be split into prime numbers, each of which is in the range 2 to 100 inclusive. Since the answer can be large, return the answer modulo 109 + 7. Note: A partition that contains numbers with leading zeroes will be invalid and the initial string does not contain leading zeroes. Take for example the input string to be s = "11373", then this string can be split into 6 different ways as [11, 37, 3), [113, 7, 3), [11, 3, 73), [11, 37, 3), (113, 73) and [11, 373) where each one of them contains only prime numbers.
"""

from time import sleep


def count_ways_to_split_Prime(string: str) -> int:
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, num-1):
            if num % i == 0:
                return False
        return True

    def dfs(string: str, target: str, count: int):
        print("残り", len(string), string)
        if len(string) == 0:
            print('@@@@@@@@@@@@@@@@@@@@@')
            count += 1
            return
        if not is_prime(int(target)):
            print("Not Prime: ", target)
            print("count: ", count)
            print()
            sleep(2)
            return
        for i in range(1, len(string)+1):
            print("index:", i)
            print("Prime: ", target)
            print("count: ", count)
            print()
            sleep(2)


            dfs(string[i:], string[:i], count)



    count: int = 0
    for i in range(1, len(string)+1):
        dfs(string, string[:i], count)

    print(count)
    return count

if __name__ == "__main__":
    # given: str = "11373"
    given: str = "31173"
    count_ways_to_split_Prime(given)
