/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return build(nums, 0, nums.size() - 1);
    }
    
    TreeNode *build(vector<int> &nums, int low, int high) {
        if (low > high) return NULL;
        int mid = (low + high) / 2;
        TreeNode *root = new TreeNode(nums[mid]);
        root -> left = build(nums, low, mid - 1);
        root -> right = build(nums, mid + 1, high);
        return root;
    }
};
