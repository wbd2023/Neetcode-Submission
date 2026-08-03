class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)
        max_odd, min_even = 0, len(s)

        for _, count in counts.items():
            if count % 2 == 1:
                max_odd = max(max_odd, count)
            else:
                min_even = min(min_even, count)

        return max_odd - min_even
