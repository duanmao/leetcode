// Time: O(n^2), space: O(n)
class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        unordered_map<int, int> ab;
        for (int a : A) for (int b : B) ++ab[a + b];
        int count = 0;
        for (int c : C) for (int d : D) if (ab[-c-d]) count += ab[-c-d];
        return count;
    }
};
