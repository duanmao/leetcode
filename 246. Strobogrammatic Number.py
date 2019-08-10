class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {'6':'9', '9':'6', '8':'8', '1':'1', '0':'0'}
        left, right = 0, len(num) - 1
        while (left <= right):
            if (num[left] not in mapping or 
                not mapping[num[left]] == num[right]):
                return False
            left += 1
            right -= 1
        return True
