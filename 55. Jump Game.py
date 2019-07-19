# Time: O(n), space: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reached = current = 0
        while (current <= reached and reached < len(nums) - 1):
            reached = max(reached, current + nums[current])
            current += 1
        return reached >= len(nums) - 1

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if (len(nums) < 2):
            return True
        cur = len(nums) - 2
        while (cur >= 0):
            if (nums[cur] == 0):
                # cannot step forward from here
                # need to find a previous position that can reach the next position
                minStep = 1
                while (cur >= 0 and nums[cur] < minStep):
                    minStep += 1
                    cur -= 1
                if (cur < 0):
                    return False
            else:
                cur -= 1
        return True
