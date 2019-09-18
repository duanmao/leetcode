# Time: O(n), space: O(1)
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def rotate(target):
            counta = countb = 0
            for i in range(len(A)):
                if (A[i] != target and B[i] != target):
                    return float('inf')
                if (A[i] != target): counta += 1
                elif (B[i] != target): countb += 1
            return min(counta, countb)

        res = min(rotate(A[0]), rotate(B[0]))
        return res if res < float('inf') else -1

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def rotate(target):
            if not all(a == target or b == target for a, b in zip(A, B)):
                return float('inf')
            return min(len(A) - A.count(target), len(B) - B.count(target))

        res = min(rotate(A[0]), rotate(B[0]))
        return res if res < float('inf') else -1


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
# namely the first two implementations
