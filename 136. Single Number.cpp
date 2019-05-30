// A XOR A = 0; XOR is commutative; 0 XOR A = A
// Therefore, XOR all elements: those appeared twice gets 0 eventually
// Only the unique one will be left
// Time complexity O(n), space complexity O(1)

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int num = 0;
        for (int i = 0; i < nums.size(); ++i) {
            num ^= nums[i];
        }
        
        return num;
    }
};
