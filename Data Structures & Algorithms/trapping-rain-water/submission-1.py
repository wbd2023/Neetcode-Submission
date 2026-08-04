class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        result = 0
        moved = []

        while left < right:
            area = self.area(height, left, right)
            area -= sum([height[blocked] * 1 for blocked in moved])

            result = max(result, area)
            result += area if area < 0 else 0

            print(left, right, area)
            
            if height[left] < height[right]:
                left += 1
                moved = [left]
                continue

            if height[left] == height[right]:
                left, right = left + 1, right - 1
                moved = [left, right]
                continue

            if height[left] > height[right]:
                right -= 1
                moved = [right]
                continue

        return result

    def area(self, height: List[int], left: int, right: int) -> int:
        return min(height[left], height[right]) * abs(right - left)
