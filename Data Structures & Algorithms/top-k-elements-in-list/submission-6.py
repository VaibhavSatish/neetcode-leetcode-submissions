class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = defaultdict(int)
        for num in nums:
            nums_map[num]+=1
        
        sorted_dict = dict(sorted(nums_map.items(), key=lambda item: item[1], reverse = True))

        return list(sorted_dict.keys())[:k]