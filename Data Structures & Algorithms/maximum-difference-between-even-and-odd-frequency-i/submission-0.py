class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)
        max_even, max_odd = 0, 0

        for count in counts.values():
            if count % 2 == 0:
                max_even = max(max_even, count)
            else:
                max_odd = max(max_odd, count)

        return abs(max_even - max_odd)
