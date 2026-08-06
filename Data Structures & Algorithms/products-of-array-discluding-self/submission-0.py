class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        to_skip_index = 0
        while to_skip_index < len(nums):
            current_product = 1
            for i in range(len(nums)):
                if (i == to_skip_index):
                    continue
                else:
                    current_product = current_product*nums[i]
            arr.append(current_product)
            to_skip_index+=1
        return arr
