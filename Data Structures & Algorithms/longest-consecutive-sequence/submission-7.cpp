class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int length = 1;
        int max_length = 1;
        set<int>no_dup(nums.begin(), nums.end());
        vector<int>no_dups(no_dup.begin(), no_dup.end());
        int nums_length = no_dups.size();
        if (nums_length == 0){
            return 0;
        }
        sort(no_dups.begin(), no_dups.end());
        for (int i = 0; i<nums_length-1; ++i){
            if(no_dups[i]+1==no_dups[i+1]){
                length++;
            }
            else{
                length = 1;
            }
            if (length > max_length){
                max_length = length;
            }
        }
        return max_length;
    }
};
