// 中文解释见1楼：https://leetcode.com/problems/find-the-duplicate-number/discuss/72934/Share-my-solution-O(N)-time-O(1)-space.-12-ms
// https://leetcode.com/problems/find-the-duplicate-number/discuss/72846/My-easy-understood-solution-with-O(n)-time-and-O(1)-space-without-modifying-the-array.-With-clear-explanation.
// 时间：O(n), 空间：O(1)
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        if (nums.size() <= 1) return 0;
        int slow = nums[0];
        int fast = nums[nums[0]];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        
        fast = 0;
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        
        return slow;
    }
};

// 这个方法其实比上面的更难写，二分坑多……
// 时间：O(NlogN)，空间：O(1)
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int low = 0, high = nums.size() - 1;
        while (low < high) { // 坑1
            int mid = (low + high) / 2;
            int count = 0;
            for (int num : nums) if (num <= mid) ++count;
            if (count <= mid) low = mid + 1; // 坑2
            else high = mid; // 坑3
        }
        
        return low;
    }
};
