// 这个方法太牛逼了！惊为天人！
// 完全利用了出现次数 *大于* n/2的条件
// http://www.cs.utexas.edu/~moore/best-ideas/mjrty
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0, major = 0;
        for (int num : nums) {
            if (count == 0) {
                major = num;
                ++count;
            } else if (major == num) {
                ++count;
            } else {
                --count;
            }
        }
        
        return major;
    }
};

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> dict;
        int maxfreq = 0;
        for (int num : nums) {
            ++dict[num];
            maxfreq = max(maxfreq, dict[num]);
        }
        
        vector<int> bucket(maxfreq + 1);
        for (auto kv : dict) bucket[kv.second] = kv.first;
        return bucket[maxfreq];
    }
};
