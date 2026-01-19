class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int sz=nums.size()+2;
        vector<int>pre(sz,0),suf(sz,0);
        for(int i=1;i<=nums.size();i++){
            pre[i]=pre[i-1]+nums[i-1];
        }
        for(int i=nums.size();i>=1;i--){
            suf[i]=suf[i+1]+nums[i-1];
        }
        for(int i=1;i<=nums.size();i++){
            if(pre[i-1]==suf[i+1]) return i-1;
        }
        return -1;
    }
};