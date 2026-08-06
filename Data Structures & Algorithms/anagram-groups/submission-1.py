class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}
        for word in strs:
            if "".join(sorted(word)) not in word_map:
                word_map["".join(sorted(word))] = []
            word_map["".join(sorted(word))].append(word)
    
        return list(word_map.values())
            

        
