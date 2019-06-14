/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class NestedIterator {
private: 
    vector<int> list;
    int ptr = 0;
    
    vector<int> breakList(vector<NestedInteger> nested) {
        vector<int> flat;
        for (auto cur: nested) {
            if (cur.isInteger()) {
                flat.push_back(cur.getInteger());
            } else {
                vector<int> curFlat = breakList(cur.getList());
                flat.insert(flat.end(), curFlat.begin(), curFlat.end());
            }
        }
        
        return flat;
    }
    
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        ptr = 0;
        list = breakList(nestedList);
    }

    int next() {
        return list[ptr++];
    }

    bool hasNext() {
        return ptr != list.size();
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
