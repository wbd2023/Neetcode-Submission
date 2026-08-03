class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        heap = []

        for count, letter in [(a, "a"), (b, "b"), (c, "c")]:
            if count > 0:
                heapq.heappush_max(heap, (count, letter))

        # Greedily use the most common legal letter. Less common letters act as separators,
        # so using them unnecessarily can make the dominant letter harder to place later.
        while heap:
            count1, letter1 = heapq.heappop_max(heap)

            # If the most common letter is blocked, use the next most common letter as a separator.
            if len(result) >= 2 and result[-2] == result[-1] == letter1:
                if not heap:
                    break

                count2, letter2 = heapq.heappop_max(heap)

                result.append(letter2)
                count2 -= 1

                if count2 > 0:
                    heapq.heappush_max(heap, (count2, letter2))

                heapq.heappush_max(heap, (count1, letter1))
                continue

            result.append(letter1)
            count1 -= 1

            if count1 > 0:
                heapq.heappush_max(heap, (count1, letter1))

        return "".join(result)
