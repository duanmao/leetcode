// 中序遍历，记录已经访问过的节点个数，每经过一个节点记录一次
// 在当前节点，若已经访问过的节点刚好为k个，此节点即为目标
// 否则继续遍历

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
    int kthSmallest(TreeNode* root, int k) {
        int count = 0;
        int ksmall = 0;
        kth(root, count, k, ksmall);
        return ksmall;
    }
    
    void kth(TreeNode *node, int &count, int k, int &ksmall) {
        if (!node) return;
        kth(node -> left, count, k, ksmall);
        ++count;
        if (count == k) ksmall = node -> val;
        else kth(node -> right, count, k, ksmall);
    }
};
