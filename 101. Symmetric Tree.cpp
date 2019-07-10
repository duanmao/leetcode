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
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        return equal(root -> left, root -> right);
    }
    
    bool equal(TreeNode *inLeft, TreeNode *inRight) {
        if (!inLeft && !inRight) return true;
        else if (!inLeft || !inRight) return false;
        if (inLeft -> val != inRight -> val) return false;
        return equal(inLeft -> left, inRight -> right) && equal(inLeft -> right, inRight -> left);
    }
};
