class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            for subset in result.copy():
                new = subset.copy()
                new.append(num)
                result.append(new)

        return result
