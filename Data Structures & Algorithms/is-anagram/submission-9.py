class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for char in s:
            letters[char] = letters.get(char, 0)+1
        
        for char in t:
            if char in letters:
                letters[char]-=1
            else:
                return False

        return max(letters.values()) == 0