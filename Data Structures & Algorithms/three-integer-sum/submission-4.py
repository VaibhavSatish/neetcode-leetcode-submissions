class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        final = []
        for i in range(size):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = size-1
            while (left < right): 
                temp = []
                if nums[i] + nums[left] + nums[right] == 0 and left != right:
                    temp.append(nums[i])
                    temp.append(nums[left])
                    temp.append(nums[right])
                    left+=1
                    right-=1
                    final.append(temp)
                    while left < right and nums[left] == nums[left-1]:
                            left+=1
                    while left < right and nums[right] == nums[right+1]:
                            right-=1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left+=1
                else:
                    right-=1
        return final
            
