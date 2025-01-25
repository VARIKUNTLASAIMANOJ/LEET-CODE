class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        indexed_nums = sorted((num, i) for i, num in enumerate(nums))
        result = [0] * n
        stack = []
        for value, idx in indexed_nums:
            if stack and abs(nums[stack[-1]] - value) > limit:
                self.sort_and_place(nums, stack, result)
                stack = []
            stack.append(idx)
        if stack:
            self.sort_and_place(nums, stack, result)
        return result
    def sort_and_place(self, nums, indices, result):
        values = sorted(nums[i] for i in indices)
        indices.sort()
        for i, val in zip(indices, values):
            result[i] = val