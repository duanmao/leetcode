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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return build(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);
    }
    
    TreeNode* build(vector<int> &preorder, int plow, int phigh, vector<int> &inorder, int ilow, int ihigh) {
        if (plow > phigh || ilow > ihigh) return NULL;
        int val = preorder[plow];
        TreeNode *root = new TreeNode(val);
        int ipos;
        for (ipos = 0; ipos < inorder.size(); ++ipos) if (inorder[ipos] == val) break;
        root -> left = build(preorder, plow + 1, plow + ipos - ilow, inorder, ilow, ipos - 1);
        root -> right = build(preorder, plow + ipos - ilow + 1, phigh, inorder, ipos + 1, ihigh);
        return root;
    }
};
