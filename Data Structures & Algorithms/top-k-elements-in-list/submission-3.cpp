class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> frequencies;
        vector<pair<int, int>> arr;
        vector<int> most_frequent;
        for (int i : nums){
            frequencies[i]++;
        }
        for (auto p : frequencies){
            arr.push_back(p);
        }
        sort(arr.begin(), arr.end(), [](const auto& left, const auto& right) {
        return left.second > right.second;
    });
        for (int i = 0; i<k; ++i){
            most_frequent.push_back(arr[i].first);
        }
        return most_frequent;
    }
};
