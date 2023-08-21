'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

Solution:

Runtime
32ms
Beats 95.37% of users with Python3

Memory
16.21MB
Beats 68.35% of users with Python3
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        c = []
        if needle in haystack:
            for i, char in enumerate(haystack):
                c.append(char)
                if needle in ''.join(c):
                    return i - len(needle) + 1
        else:
            return -1

solution = Solution()

test_cases = [
    ["sadbutsad", "sad"],
    ["leetcode", "leeto"],
    ["hello", 'll'],
    ["a", "a"]
]

for testCase in test_cases:
    print(solution.strStr(*testCase))
