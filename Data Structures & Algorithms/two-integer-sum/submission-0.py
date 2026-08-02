class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} #value:index
        for i in range(len(nums)):
            if target - nums[i] in indices:
                return sorted([i, indices[target - nums[i]]])
            else:
                indices[nums[i]] = i
        return None

        