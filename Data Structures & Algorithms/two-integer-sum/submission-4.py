class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_dict = {}
        for i in enumerate(nums):
            val_dict[i[1]] = i[0]
        
        for j in range(len(nums)):
            value = target-nums[j]
            if value in val_dict and val_dict[value] != j:
                return [j, val_dict[value]]

        return -1

