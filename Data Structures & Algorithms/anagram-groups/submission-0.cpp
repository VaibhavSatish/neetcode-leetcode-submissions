class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()){
            return false;
        }
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        return s == t;
    }

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> anagrams; 
        for (int i = 0; i<strs.size(); ++i){
            vector<string> group;
            for (int j = 0; j<strs.size(); ++j){
                if (isAnagram(strs[i], strs[j])){
                    group.push_back(strs[j]);
                }
            }
            anagrams.push_back(group);
        }
        set<vector<string>> remove_duplicates(anagrams.begin(), anagrams.end());
        vector<vector<string>> anagrams_no_dup(remove_duplicates.begin(), remove_duplicates.end());
        return anagrams_no_dup; 
    }
};
