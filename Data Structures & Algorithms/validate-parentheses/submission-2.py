class Solution:
    def isValid(self, s: str) -> bool:
        BRACKET_PAIRS = {"(": ")", "{": "}", "[": "]"}

        stack = []

        for char in s:
            print(char)
            print(stack)
            print()

            if char in BRACKET_PAIRS.keys():
                stack.append(BRACKET_PAIRS[char])
                continue

            if not stack or stack[-1] != char:
                return False

            stack.pop()

        if stack:
            return False

        return True
