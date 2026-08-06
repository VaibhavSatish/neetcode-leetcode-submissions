class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = defaultdict(int)
        for num in nums:
            nums_map[num]+=1
        
        nums_map = dict(sorted(nums_map.items(), key=lambda item: item[1], reverse = True))

        return list(nums_map.keys())[:k]