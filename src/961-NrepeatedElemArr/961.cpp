/class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        std::map<int, int> hash;
        for (int n : nums) {
            hash[n]++;
        }
        for (auto& x : hash) {
            if (x.second != 1) return x.first;
        }
        return 0;
    }
};/ Solution
