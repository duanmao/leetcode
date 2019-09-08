// Union Find
// Time: O(n^2 * l), space: O(n)
// but still extremely slow
class Solution {
private:
    map<int, int> parent;
    int group;
    
    // w1 and w2 are already anagrams
    bool similar(string &w1, string &w2) {
        int diffs = 0;
        for (int i = 0; i < w1.size(); ++i) {
            if (w1[i] != w2[i]) diffs += 1;
            if (diffs > 2) return false;
        }
        
        return true;
    }
    
    int find(int x) {
        if (parent.count(x) == 0) parent[x] = x;
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    
    void unite(int x, int y) {
        int rootx = find(x), rooty = find(y);
        if (rootx != rooty) {
            group -= 1;
            parent[rootx] = rooty;
        }
    }
    
public:
    int numSimilarGroups(vector<string>& A) {
        int n = A.size();
        parent = map<int, int>();
        group = n;
        
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (similar(A[i], A[j])) unite(i, j);
            }
        }
        
        return group;
    }
};
