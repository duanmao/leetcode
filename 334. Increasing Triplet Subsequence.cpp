// Time: O(n), space: O(1)
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int min = INT_MAX, secondMin = INT_MAX;
        for (int num : nums) {
            if (num <= min) min = num;
            else if (num <= secondMin) secondMin = num;
            else return true; // num > secondMin
        }
        
        return false;
    }
};
