class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        length = math.gcd(len(str1), len(str2))
        result = str1[:length]

        for i, char in enumerate(str1):
            if char != result[i % length]:
                return ""

        for i, char in enumerate(str2):
            if char != result[i % length]:
                return ""

        return result
