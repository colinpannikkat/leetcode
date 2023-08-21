class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        c = list(s) # turn s to list

        # find all substrings, determine if it can be built into string
        while len(c) > 0:
            subString = ''.join(s[len(c)//2:])
            if subString != s and len(s) % len(subString) == 0 and subString*(int(len(s)/len(subString))) == s:
                return True
            c.pop()
            
        return False
    
solution = Solution()

test_cases = [
    "abab",
    "aba",
    "abcabcabcabc",
    "a"
]

for testCase in test_cases:
    print(solution.repeatedSubstringPattern(testCase))