class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            # Copy the outer list so appending to result does not extend this iteration.
            for subset in result.copy():
                # Copy the inner list so modifying new does not modify subset inside result.
                new = subset.copy()

                # append() modifies new in place and returns None.
                new.append(num)

                # Append the modified list itself, rather than new.append()'s return value.
                result.append(new)

        return result
