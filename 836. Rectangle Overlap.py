class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # rec1 is on the right or left of rec2
        if rec1[0] >= rec2[2] or rec1[2] <= rec2[0]: return False
        # rec1 is above or below rec2
        if rec1[1] >= rec2[3] or rec1[3] <= rec2[1]: return False
        return True

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # project onto axes. to overlap
        # the smaller of (the largest x-coordinates) should be larger than the larger of (the smallest x-coordinates)
        # and the same to y-coordinates
        return (min(rec1[2], rec2[2]) > max(rec1[0], rec2[0]) and
                min(rec1[3], rec2[3]) > max(rec1[1], rec2[1]))
