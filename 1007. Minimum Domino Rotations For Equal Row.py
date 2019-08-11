# Time: O(n), space: O(1)
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        for x in range(1, 7):
            if all(x == a or x == b for a, b in zip(A, B)):
                return min(len(A) - A.count(x), len(B) - B.count(x))
        return -1

# verbose but possibly easier to understand, basically the same idea
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def rotate(inA, withB, target):
            count = 0
            for i, a in enumerate(inA):
                if (not a == target):
                    if (withB[i] == target):
                        count += 1
                    else:
                        return float('inf')
            return count
        
        minrot = float('inf')
        for i in range(1, 7):
            minrot = min(minrot, rotate(A, B, i))
            minrot = min(minrot, rotate(B, A, i))
        return minrot if minrot < float('inf') else -1

# Go further, we actually only need to check for A[0] and B[0] instead of [1, 6]
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def rotate(A, B, target):
            if (all(target == a or target == b for a, b in zip(A, B))):
                return min(len(A) - A.count(target), len(B) - B.count(target))
            return float('inf')

        minrot = rotate(A, B, A[0])
        minrot = min(minrot, rotate(A, B, B[0]))
        return minrot if minrot < float('inf') else -1
