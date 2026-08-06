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
        if (s_map.size() != t_map.size()){
            return false;
        }
        for (pair mm : s_map){
            if (s_map[mm.first] != t_map[mm.first]){
                return false;
            }
        }
        return true;
    }
};
