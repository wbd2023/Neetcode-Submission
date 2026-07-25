class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        first, second = self.wrapper(left, heights[left]), self.wrapper(right, heights[right])

        while left < right:
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1

            if self.area(self.wrapper(left, heights[left]), self.wrapper(right, heights[right])) > self.area(first, second):
                first, second = self.wrapper(left, heights[left]), self.wrapper(right, heights[right])

        return self.area(first, second)


    @staticmethod
    def wrapper(index: int, height: int) -> Dict[str, int]:
        return {"index": index, "height": height}


    @staticmethod
    def area(first: Dict[str, int], second: Dict[str, int]) -> int:
        distance = abs(first["index"] - second["index"])
        height = min(first["height"], second["height"])
        return distance * height
