// Time complexity: O(n), space complexity: O(n)
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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> nums;
        stack<TreeNode *> s;
        TreeNode *cur = root;
        while (cur || !s.empty()) {
            while (cur) {
                s.push(cur);
                cur = cur -> left;
            }
            
            cur = s.top();
            s.pop();
            nums.push_back(cur -> val);
            
            // ATTENTION here!
            cur = cur -> right;
        }
        
        return nums;
    }
};

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> nums;
        inorder(root, nums);
        return nums;
    }
    
    void inorder(TreeNode *node, vector<int> &nums) {
        if (!node) return;
        inorder(node -> left, nums);
        nums.push_back(node -> val);
        inorder(node -> right, nums);
    }
};
