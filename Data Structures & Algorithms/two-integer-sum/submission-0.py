class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        possibilities = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference in possibilities:
                return [possibilities[difference], index]
            possibilities[value] = index 
        return []


        