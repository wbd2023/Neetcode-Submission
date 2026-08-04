class Solution:
    def isValid(self, s: str) -> bool:
        BRACKET_PAIRS = {"(": ")", "{": "}", "[": "]"}

        stack = []

        for char in s:
            if char in BRACKET_PAIRS.keys():
                stack.append(BRACKET_PAIRS[char])
                continue

            if stack and stack[-1] == char:
                stack.pop()
                continue

            return False

        return True if not stack else False
