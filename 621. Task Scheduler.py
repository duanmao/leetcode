# Time: O(n), space: O(1)
# https://leetcode.com/problems/task-scheduler/discuss/104500/Java-O(n)-time-O(1)-space-1-pass-no-sorting-solution-with-detailed-explanation
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounts = sorted(list(Counter(tasks).values()), reverse = True)
        parts = taskCounts[0]
        # number of tasks with the highest frequency
        bundle = sum([1 for c in taskCounts if c == taskCounts[0]])
        # remaining slots that need to be filled with other tasks
        # in each part, there're (n + 1 - bundle) slots
        # the last part does not need to be filled
        emptySlots = (n - bundle + 1) * (parts - 1)
        # number of remaining tasks (tasks that are less frequent)
        leftTasks = len(tasks) - parts * bundle
        # fill empty slots with other tasks, if not enough, we need idle slots
        idle = max(0, emptySlots - leftTasks)
        return len(tasks) + idle

# Time: O(n), space: O(1)
# https://leetcode.com/problems/task-scheduler/discuss/104501/Java-PriorityQueue-solution-Similar-problem-Rearrange-string-K-distance-apart
import collections
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounts = [-v for v in collections.Counter(tasks).values()]
        heapq.heapify(taskCounts) # minheap
        intervals = 0
        while taskCounts:
            schedule = 1 + n
            moreTasks = []
            while schedule and taskCounts:
                t = heapq.heappop(taskCounts)
                schedule -= 1 # scheduled one task
                if -t > 1: moreTasks.append(t + 1)
            for t in moreTasks:
                heapq.heappush(taskCounts, t)
            intervals += 1 + n
            if not taskCounts: intervals -= schedule # no more tasks, no more idle needed
        return intervals
