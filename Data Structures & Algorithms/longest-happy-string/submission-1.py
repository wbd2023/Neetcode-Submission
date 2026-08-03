class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        heap = []

        for count, letter in [(a, "a"), (b, "b"), (c, "c")]:
            if count > 0:
                heapq.heappush_max(heap, (count, letter))

        while heap:
            count1, letter1 = heapq.heappop_max(heap)

            # Use the next most common letter if the first would form a triple.
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
