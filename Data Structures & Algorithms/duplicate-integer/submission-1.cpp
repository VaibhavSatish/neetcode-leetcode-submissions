class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int>non_duplicates(nums.begin(), nums.end());
        return nums.size() != non_duplicates.size();
    }
};