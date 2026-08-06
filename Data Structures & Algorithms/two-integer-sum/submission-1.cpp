class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> sum_finder;
        vector<int>values;
        for (int i = 0; i<nums.size(); ++i){
            int diff = target - nums[i];
            if (sum_finder.find(diff) != sum_finder.end()){
                values.push_back(sum_finder[diff]);
                values.push_back(i);
                return values; 
            }
            sum_finder.insert({nums[i], i});
        }
        return values;
    }
};
