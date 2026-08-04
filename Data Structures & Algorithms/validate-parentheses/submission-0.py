class Solution:
    def isValid(self, s: str) -> bool:
        BRACKET_PAIRS = {"(": ")", "{": "}", "[": "]"}

        stack = []

        for char in s:
            if char in BRACKET_PAIRS.keys():
                stack.append(BRACKET_PAIRS[char])
                continue

            if not stack and stack[-1] != char:
                return False

            stack.pop()

        return True
