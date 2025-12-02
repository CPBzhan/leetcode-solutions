using namespace std;

class Solution {
public:
    int countTrapezoids(vector<vector<int>>& points) {
        const long long MOD = 1e9 + 7;

        unordered_map<int, long long> cnt;
        for (auto &p : points) {
            cnt[p[1]]++;
        }

        long long sumSeg = 0;     // sum of C(c,2)
        long long sumSeg2 = 0;    // sum of C(c,2)^2

        for (auto &kv : cnt) {
            long long c = kv.second;
            if (c >= 2) {
                long long s = c * (c - 1) / 2;  // C(c,2)
                s %= MOD;
                sumSeg = (sumSeg + s) % MOD;
                sumSeg2 = (sumSeg2 + s * s) % MOD;
            }
        }

        if (sumSeg == 0) return 0;

        long long ans = (sumSeg * sumSeg % MOD - sumSeg2 + MOD) % MOD;
        ans = ans * ((MOD + 1) / 2) % MOD;

        return ans;
    }
};// Solution
