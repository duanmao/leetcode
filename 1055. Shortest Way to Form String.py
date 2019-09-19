# https://leetcode.com/problems/shortest-way-to-form-string/discuss/330938/Accept-is-not-enough-to-get-a-hire.-Interviewee-4-follow-up
# Time: O(m + n), space: O(n)
# https://leetcode.com/problems/shortest-way-to-form-string/discuss/332419/O(M-%2B-N)-Java-solution-with-commented-code-and-detailed-explanation-(Beats-98)
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        def idx(c):
            return ord(c) - ord('a')

        n = len(source)
        # indices[l][c]: starting from pos l, the first occurrence of char c
        indices = [[-1] * 26 for i in range(n)]
        for i in range(n)[::-1]:
            if (i < n - 1): indices[i] = indices[i + 1][:]
            indices[i][idx(source[i])] = i
        pos = 0
        use = 1
        for c in target:
            if (indices[0][idx(c)] == -1): return -1
            if (pos >= n or indices[pos][idx(c)] == -1):
                use += 1
                pos = indices[0][idx(c)] + 1
            else:
                pos = indices[pos][idx(c)] + 1
        return use

# Time: O(mlogn), m: len(target), n: len(source); Space: O(n)
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        def binarys(indices, pre):
            low, high = 0, len(indices) - 1
            while (low <= high):
                mid = (low + high) // 2
                if (indices[mid] > pre): high = mid - 1
                else: low = mid + 1
            return indices[low] if low < len(indices) else -1

        indices = collections.defaultdict(list)
        for i, c in enumerate(source):
            indices[c].append(i)
        pre = -1
        use = 1
        for i, c in enumerate(target):
            if (c not in indices): return -1
            pre = binarys(indices[c], pre)
            if (pre == -1):
                use += 1
                pre = indices[c][0]
            # or use built-in bisect
            # nxt = bisect.bisect(indices[c], pre)
            # if (nxt == len(indices[c])):
            #     use += 1
            #     nxt = 0
            # pre = indices[c][nxt]
        return use

# Time: O(mn) where m is the length of target, n is the length of source
# Space: O(1)
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        cur = 0
        lens = len(source)
        for i, c in enumerate(target):
            last = cur
            while cur < last + lens and c != source[cur % lens]:
                cur += 1
            if (cur == last + lens): return -1
            cur += 1
        return cur // lens + bool(cur % lens)

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        ptr_t = 0
        use = 0
        while (ptr_t < len(target)):
            last_t = ptr_t
            for c in source:
                if (ptr_t < len(target) and target[ptr_t] == c):
                    ptr_t += 1
            if (last_t == ptr_t): return -1
            use += 1
        return use

# Time: O(m + 26n)
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        n = len(source)
        indices = {}
        for i, c in enumerate(source):
            if (c not in indices): indices[c] = [-1] * (n + 1)
            indices[c][i - 1] = i # the next position of char c after pos i - 1 is i
        for c in indices:
            for i in range(-1, n - 1)[::-1]:
                if (indices[c][i] == -1): indices[c][i] = indices[c][i + 1]
        pre = -1
        use = 1
        for c in target:
            if (c not in indices): return -1
            pos = indices[c][pre]
            if (pos < pre):
                use += 1
                pre = indices[c][-1]
            else:
                pre = pos
        return use
