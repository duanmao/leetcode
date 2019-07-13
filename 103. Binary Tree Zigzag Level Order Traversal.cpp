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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> vals;
        if (!root) return vals;
        queue<TreeNode*> q;
        q.push(root);
        bool order = true;
        while (!q.empty()) {
            int size = q.size();
            vector<int> level(size);
            for (int i = 0; i < size; ++i) {
                TreeNode *node = q.front();
                q.pop();
                if (order) level[i] = node -> val;
                else level[size - i - 1] = node -> val;
                if (node -> left) q.push(node -> left);
                if (node -> right) q.push(node -> right);
            }

            vals.push_back(level);
            order = !order;
        }

        return vals;
    }
};

class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> vals;
        if (!root) return vals;
        vector<int> levelvals;
        vector<pair<TreeNode*, int>> rd, wr;
        rd.push_back(mkpr(root, 1));
        int level = 1;
        int ptr = 0;
        while (!rd.empty()) {
            TreeNode *cur = rd[ptr].first;
            int curlevel = rd[ptr].second;
            if (curlevel % 2 == 1) {
                leftRight(wr, cur, curlevel);
            } else {
                rightLeft(wr, cur, curlevel);
            }
            
            levelvals.push_back(cur -> val);
            --ptr;
            
            if (ptr < 0) {
                rd = wr;
                wr.clear();
                vals.push_back(levelvals);
                levelvals.clear();
                ptr = rd.size() - 1;
            }
        }
        
        return vals;
    }
    
    pair<TreeNode*, int> mkpr(TreeNode *node, int level) {
        return pair<TreeNode*, int>(node, level);
    }
    
    void leftRight(vector<pair<TreeNode*, int>> &q, TreeNode *node, int level) {
        if (node -> left) q.push_back(mkpr(node -> left, level + 1));
        if (node -> right) q.push_back(mkpr(node -> right, level + 1));
    }
    
    void rightLeft(vector<pair<TreeNode*, int>> &q, TreeNode *node, int level) {
        if (node -> right) q.push_back(mkpr(node -> right, level + 1));
        if (node -> left) q.push_back(mkpr(node -> left, level + 1));
    }
};
