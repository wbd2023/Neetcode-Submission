class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        first, second = wrapper(left, heights[left]), wrapper(right, heights[right])

        while left < right:
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1

            x, y = wrapper(left, heights[left]), wrapper(right, heights[right])
            if area(x, y) > area(first, second):
                first, second = x, y

        return area(first, second)


def wrapper(index: int, height: int) -> Dict[str, int]:
    return {"index": index, "height": height}


def area(first: Dict[str, int], second: Dict[str, int]) -> int:
    distance = abs(first["index"] - second["index"])
    height = min(first["height"], second["height"])
    return distance * height
