// C++ 用到swap就RE，很费解，于是只好用python了
// 时间复杂度O(n)，空间复杂度O(1)

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        head = 0
        tail = len(s) - 1
        while head < tail:
            s[head], s[tail] = s[tail], s[head]
            head += 1
            tail -= 1
