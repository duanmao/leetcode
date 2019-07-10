// Time: O(n), space: O(n)
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        vector<int> left(n, 0), right(n, 0);
        for (int i = 1; i < n; ++i) left[i] = max(height[i - 1], left[i - 1]);
        for (int i = n - 2; i >= 0; --i) right[i] = max(height[i + 1], right[i + 1]);
        int water = 0;
        for (int i = 0; i < n; ++i) water += max(0, min(left[i], right[i]) - height[i]);
        return water;
    }
};
