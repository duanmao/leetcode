// Time: O(m + n), space: O(m)
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> its;
        unordered_map<int, int> dict;
        for (int num: nums1) dict[num]++;
        for (int num: nums2) if(dict.find(num) != dict.end() && dict[num]-- > 0) its.push_back(num);
        return its;
    }
};

// If sorted, assume the sorted arrays are given
// Time: O(m + n), space: O(1)
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        vector<int> its;
        int ptr1 = 0, ptr2 = 0;
        int m = nums1.size(), n = nums2.size();
        while (ptr1 < m && ptr2 < n) {
            if (nums1[ptr1] == nums2[ptr2]) {
                its.push_back(nums1[ptr1++]);
                ++ptr2;
            } else if (nums1[ptr1] < nums2[ptr2]) {
                ++ptr1;
            } else {
                ++ptr2;
            }
        }

        return its;
    }
};
