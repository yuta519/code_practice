"""
count the number of ways the string can split to get pime number

Given a string of length n consisting of digits [0-9], count the number of ways the given string can be split into prime numbers, each of which is in the range 2 to 100 inclusive. Since the answer can be large, return the answer modulo 109 + 7. Note: A partition that contains numbers with leading zeroes will be invalid and the initial string does not contain leading zeroes. Take for example the input string to be s = "11373", then this string can be split into 6 different ways as [11, 37, 3), [113, 7, 3), [11, 3, 73), [11, 37, 3), (113, 73) and [11, 373) where each one of them contains only prime numbers.
"""

def countWaysToSplitPrime(string: str) -> int:

    return

if __name__ == "__main__":
    given: str = "11373"
    print(countWaysToSplitPrime(given))
