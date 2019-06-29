// Space: O(1)
class Solution {
public:
    bool isHappy(int n) {
        int slow = n, fast = n;
        do {
            slow = digitsSqrdSum(slow);
            fast = digitsSqrdSum(digitsSqrdSum(fast));
            if (fast == 1) return true;
        } while (slow != fast);
        
        return false;
    }
    
    int digitsSqrdSum(int n) {
        int sum = 0;
        for (int i = n; i > 0; i /= 10) sum += (i % 10) * (i % 10);
        return sum;
    }
};

// Extra space
class Solution {
public:
    bool isHappy(int n) {
        set<int> mark;
        int cur = n;
        while (mark.count(1) < 1 && mark.count(cur) < 1) {
            mark.insert(cur);
            int sum = 0;
            for (int i = cur; i > 0; i /= 10) sum += (i % 10) * (i % 10);
            cur = sum;
        }
        
        return mark.count(1) > 0;
    }
};
