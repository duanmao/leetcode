# consider reading
# https://leetcode.com/problems/student-attendance-record-ii/discuss/101633/Improving-the-runtime-from-O(n)-to-O(log-n)
# and
# https://leetcode.com/problems/student-attendance-record-ii/discuss/101643/Share-my-O(n)-C%2B%2B-DP-solution-with-thinking-process-and-explanation
# when you have the mood... now I'm pretty satisfied with this O(n) solution... - -

# DP
# O(n)
class Solution:
    def checkRecord(self, n: int) -> int:
        M = 1000000007
        # f[i]: the number of rewardable records of length i that has no 'A' in it
        # thus, to compute f[i], there're 3 cases below:
        # 1. adding a 'P' => f[i - 1]
        # 2. adding 'PL' => f[i - 2]
        #       note that we cannot add 'LL' here because that will
        #       demand the control of the previous letter to be only 'P'
        #       instead of having free choices, which invalidates the derivation from f[i - 1]
        # 3. adding 'PLL' => f[i - 3]
        f = [1, 2, 4] + [0] * (n - 2)
        for i in range(3, n + 1):
            f[i] = (f[i - 1] + f[i - 2] + f[i - 3]) % M
        # count records that contain an 'A' in it
        count = 0
        for i in range(1, n + 1):
            count += (f[i - 1] * f[n - i]) % M
            count %= M
        return (f[n] + count) % M

# DFS
# Time: O(the number of valid result) - essentially O(2^n) - TLE of course
class Solution:
    def checkRecord(self, n: int) -> int:
        chars = ['A', 'L', 'P']
        self.count = 0
        
        def generate(cur, absent):
            if (len(cur) == n):
                # print(cur)
                self.count += 1
            else:
                prevabsent = absent
                for c in chars:
                    if (c == 'A'):
                        if (absent): continue
                        else: absent = True
                    elif (c == 'L'):
                        if (len(cur) >= 2 and cur[-2:] == 'LL'): continue
                    generate(cur + c, absent)
                    absent = prevabsent 
                    # note this flag must be reset every time in the loop
                    # INSTEAD OF only one time after the whole loop
                
        generate("", False)
        return self.count
