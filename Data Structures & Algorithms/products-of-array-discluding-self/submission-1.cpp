class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int>products;
        int to_skip = 0;
        int current_index = 0;
        int product = 1;
        while (to_skip < nums.size()){
            if (current_index == nums.size()){
                current_index = 0;
                to_skip++;
                products.push_back(product);
                product = 1;
            }
            else if (current_index == to_skip){
                current_index++;
                continue;
            }
            product=product*nums[current_index];
            current_index++;
        }
        return products;
    }
};
