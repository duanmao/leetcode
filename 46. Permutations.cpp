// 对排列中的第current个位置来说，假设前面已经排列完成且从此固定不变
// 那么这个位置可能出现的数字则为当前current数字及所有后面的数字
// 因此，需要将current上的数字与所有可选数字一一互换
// 每互换一次便可进行下一个位置的数字选择
// 当选择完所有数字后，即完成了一次排列，将其记录下来
// 时间复杂度：O(n!)

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> perms;
        permutations(nums, 0, perms);
        return perms;
    }
    
    void permutations(vector<int> &nums, int current, vector<vector<int> > &perms) {
        if (current == nums.size()) {
            perms.push_back(nums);
            return;
        }
        
        for (int i = current; i < nums.size(); ++i) {
            swap(nums[i], nums[current]);
            permutations(nums, current + 1, perms);
            swap(nums[i], nums[current]);
        }
    }
};
