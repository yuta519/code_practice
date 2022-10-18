"""
An item is represented as an asterisk ( * = ascii decimal 42). A compartment is represented as a pair of pipes that may or may not have items between them ( | = ascii decimal 124).

Example 1:
Input: s = |**|*|*, startIndices = [1, 1], endIndices = [5, 6]
Output: [2, 3]
Explanation:
The string has a total of 2 closed compartments, one with 2 items and one with 1 item.
For the first pair of indices, (0, 4), the substring |**|*. There are 2 items in a compartment.
For the second pair of indices, (0, 6), the substring is |**|*|* and there are 2 + 1 = 3 items in compartments.
Both of the answers are returned in an array, [2, 3]
Example 2:
Input: s = *|*|, startIndices = [1], endIndices = [3]
Output: [1]
Explanation:
the substring from index = 1 to index = 3 is |*|. There is one compartments with one item in this string.
Constraints:
1 <= m, n <= 10^5
1 <= startIndices[i] <= endIndices[i] <= n
Each character or s is either * or |
"""

import sys


def cntitems2(items: str, startIndices: list[int], endIndices: list[int]) -> list[int]:
    length = len(items)

    stars: list[int] = [0] * (length+1)
    left_most_pipe_idx = [-1] * (length+1)
    right_most_pipe_idx = [length+1] * (length+1)

    answer = []

    # pre-calc left-most pipe location and sum of stars arrays
    for i, ch in enumerate(items,1):
        if ch == "|":
            stars[i] = stars[i-1]
            left_most_pipe_idx[i] = i
        else:
            stars[i] = stars[i-1] + 1
            left_most_pipe_idx[i] = left_most_pipe_idx[i-1]

    if left_most_pipe_idx[-1] == -1:
        # When items does not have "|".
        return [0] * len(startIndices)

    # pre-calc right-most pipe location
    for i in range(length-1, -1, -1):
        if items[i] == '|':
            right_most_pipe_idx[i+1] = i + 1
        else:
            right_most_pipe_idx[i+1] = (
                right_most_pipe_idx[i+2] if i < length-1 else length+1
            )
    # calc answer as difference between num. of stars b/w right and left pipes.
    # right pipe is the left-most pipe from the end index, left pipe is the right-most one from the start index
    for i in range(len(startIndices)):
        si, ei = startIndices[i], endIndices[i]
        left_pipe = right_most_pipe_idx[si]
        right_pipe = left_most_pipe_idx[ei]
        answer.append(
            stars[right_pipe]-stars[left_pipe] if left_pipe < right_pipe else 0
        )
    return answer


def cntitems(items: str, startIndices: list[int], endIndices: list[int]) -> list[int]:
    pipe_idx: list[int] = []
    answers = []
    for idx, item in enumerate(items):
        if item == "|":
            pipe_idx.append(idx)

    if len(pipe_idx) <= 1:
        return [0] * len(startIndices)

    for i in range(0, len(startIndices)):
        array: list[int] = [i for i in range(startIndices[i]-1, endIndices[i]-1)]
        count_stars: int = 0
        for idx in range(0, len(pipe_idx)-1):
            start_idx = pipe_idx[idx] if pipe_idx[idx] in array else None
            end_idx = pipe_idx[idx+1] if pipe_idx[idx+1] in array else None
            if start_idx is not None and end_idx is not None:
                count_stars += len(array[array.index(start_idx)+1:array.index(end_idx)])
        answers.append(count_stars)
    return answers



if __name__ == '__main__':
    #  1-based index, assume start idx <= end idx, and both indices within the range 1..ln
    print(cntitems2("|**|*|*",[1,1,2],[5,7,7]))  # [2, 3, 1]
    print(cntitems2("*|**|*|**|****|*",[4,1,4],[8,16,11]))  # [1, 9, 3]
    print(cntitems2("*****|*****",[1,4,1,7],[5,8,11,9]))  # [0, 0, 0, 0]

    print(cntitems("|**|*|*", [1, 1, 2], [5, 7, 7]))  # [2, 3, 1]
    print(cntitems("*|**|*|**|****|*", [4, 1, 4], [8, 16, 11]))  # [1, 9, 3]
    print(cntitems("*****|*****",[1,4,1,7],[5,8,11,9]))  # [0, 0, 0, 0]
