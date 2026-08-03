class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = ""

        length = math.gcd(len(str1), len(str2))

        n = 0
        while n <= length - 1:
            result += str1[n]
            n += 1

        n = 0
        while n <= max(len(str1), len(str2)):
            if n <= len(str1) - 1:
                if result[n % length] != str1[n]:
                    return ""

            if n <= len(str2) - 1:
                if result[n % length] != str2[n]:
                    return ""

            n += 1

        return result
