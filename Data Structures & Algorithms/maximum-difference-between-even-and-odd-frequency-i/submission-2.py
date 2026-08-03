class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)
        max_odd, min_even = None, None

        for letter, count in counts.items():
            print(letter, count)

            if count % 2 == 1:
                max_odd = max(max_odd, count) if max_odd is not None else count
            else:
                min_even = min(min_even, count) if min_even is not None else count

        return max_odd - min_even if max_odd is not None and min_even is not None else 0
