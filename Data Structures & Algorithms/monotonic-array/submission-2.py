class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def increasing(x: int, y: int) -> bool:
            return x > y

        def decreasing(x: int, y: int) -> bool:
            return x < y

        direction = None

        for i in range(len(nums)):
            if i + 1 > len(nums) - 1:
                break

            if nums[i] == nums[i + 1]:
                continue

            if direction is None:
                if increasing(nums[i], nums[i + 1]):
                    direction = increasing
                elif decreasing(nums[i], nums[i + 1]):
                    direction = decreasing
                continue

            if not direction(nums[i], nums[i + 1]):
                return False

        return True
