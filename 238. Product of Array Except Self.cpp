// 第一遍从左往右，答案数组products里每个位置记录其左边所有元素的乘积
// 即products[i] = product(nums[0], ..., nums[i - 1])
// 同理，第二遍从右往左，只需再用一个变量right记录至今为止所有右边元素的乘积
// 并同时得到最终结果：products[i] = 左边乘积(products[i]) * 右边乘积(right)
// 时间复杂度：O(n)，空间复杂度：O(1) (不考虑最终的结果数组)
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> products(n, 1);
        
        int left = 1;
        for (int i = 1; i < n; ++i)  {
            left *= nums[i - 1];
            products[i] = left;
        }
        
        int right = nums[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            products[i] *= right;
            right *= nums[i];
        }
        
        return products;
    }
};
