class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        int i = 0;
        while (i < nums.size()) {
            if (nums[i] == 1) {
                // 检查接下来的k个位置
                for (int j = i + 1; j <= i + k && j < nums.size(); j++) {
                    if (nums[j] == 1) {
                        return false;
                    }
                }
                i += k + 1;
            } else {
                i++;
            }
        }
        return true;
    }
};// Solution
