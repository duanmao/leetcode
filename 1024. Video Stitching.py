# similar to https://leetcode.com/problems/jump-game-ii/
# Time: O(nlogn), space: O(1) 
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        res = 0
        end = 0
        i = 0
        while i < len(clips) and end < T:
            lastend = end
            if clips[i][0] > lastend: return -1 # the clips are not continuous
            # check all overlapping intervals, and choose the one that covers the furthest
            while i < len(clips) and clips[i][0] <= lastend:
                end = max(end, clips[i][1])
                i += 1
            res += 1
        return res if end >= T else -1
