class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> s_map;
        map<char, int> t_map;
        for (char ss:s){
            s_map[ss]++;
        }
        for (char tt:t){
            t_map[tt]++;
        }
        for (auto mm : s_map){
            if (t_map[mm.first] != mm.second){
                return false;
            }
        }
        return t_map.size() == s_map.size();
    }
};
