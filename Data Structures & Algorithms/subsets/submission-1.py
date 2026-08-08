class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Begin with the empty subset.
        result = [[]]

        for num in nums:
            # Take a snapshot of the existing subsets.
            # We only want to extend the subsets that existed before this iteration.
            for subset in result.copy():
                # Create a separate version of the current subset.
                new = subset.copy()

                # Include the current number in the new subset.
                new.append(num)

                # Keep the original subset and add the new version.
                result.append(new)

        return result
