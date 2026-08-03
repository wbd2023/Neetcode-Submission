class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = ""
        heap = []

        for count, letter in [(a, "a"), (b, "b"), (c, "c")]:
            if count > 0:
                heapq.heappush_max(heap, (count, letter))

        while heap:
            count1, letter1 = heapq.heappop_max(heap)

            if (
                len(result) < 2
                or not (result[-2] == result[-1] == letter1)
            ):
                result += letter1
                count1 -= 1
            else:
                if not heap:
                    return result

                count2, letter2 = heapq.heappop_max(heap)

                result += letter2
                count2 -= 1

                if count2 > 0:
                    heapq.heappush_max(heap, (count1, letter1))

            if count1 > 0:
                heapq.heappush_max(heap, (count1, letter1))

        return result
