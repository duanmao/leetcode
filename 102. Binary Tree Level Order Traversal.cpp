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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> vals;
        if (!root) return vals; // Important check
        queue<tuple<TreeNode *, int>> q;
        q.push({root, 0});
        int prelevel = 0;
        vector<int> lvals;
        while (!q.empty()) {
            auto [cur, level] = q.front();
            q.pop();
            if (cur -> left) q.push({cur -> left, level + 1});
            if (cur -> right) q.push({cur -> right, level + 1});
            if (level != prelevel) {
                vals.push_back(lvals);
                lvals.clear();
                prelevel = level;
            }
            
            lvals.push_back(cur -> val);
        }
        
        vals.push_back(lvals); // remember this step
        return vals;
    }
};
