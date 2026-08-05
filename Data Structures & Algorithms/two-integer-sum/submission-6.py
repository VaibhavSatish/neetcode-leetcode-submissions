class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, val in enumerate(nums):
            difference = target - val
            if difference in nums_map and i != nums_map[difference]:
                return [nums_map[difference], i]
            nums_map[val] = i
        return []
