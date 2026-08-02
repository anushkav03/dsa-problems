class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min = 0
        max = len(nums)
        while True:
            if min >= max:
                return -1

            guess = math.ceil(((max-min)/2) + min)
            if nums[guess] > target:
                max = guess - 1
            if nums[guess] < target:
                min = guess
            if nums[guess] == target:
                return guess


        