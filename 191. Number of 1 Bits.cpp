// Time: O(1) since uint32 only has 32 bits
// thus there can only be 32 iterations at most
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ones = 0;
        while (n != 0) {
            ones += (n & 1);
            n >>= 1;
        }
        
        return ones;
    }
};
