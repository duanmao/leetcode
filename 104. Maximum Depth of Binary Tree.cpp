// 深搜，当前节点取左右子树中的最大深度，+1 返回上一层
// 时间复杂度O(n)，空间复杂度O(1)
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
    int maxDepth(TreeNode* root) {   
        if (!root) return 0;
        return max(maxDepth(root -> left), maxDepth(root -> right)) + 1;
    }
};
