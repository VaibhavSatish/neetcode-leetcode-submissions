class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        frequent_list = []
        final_list = []
        for num in nums:
            if num in frequencies:
                frequencies[num]+=1
            else:
                frequencies[num] = 1
        for key,value in frequencies.items():
            frequent_list.append([value, key])
        frequent_list.sort()
        while len(final_list) < k:
            final_list.append(frequent_list.pop()[1])
        return final_list