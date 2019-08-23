# This problem essentially asks for an Eulerian path in a graph
# https://en.wikipedia.org/wiki/Eulerian_path
# Hierholzer's algorithm
# Time: O(E) where E is the # of edges

# https://leetcode.com/problems/reconstruct-itinerary/discuss/78835/28ms-C%2B%2B-beats-100-Short-and-Elegant.
# https://leetcode.com/problems/reconstruct-itinerary/discuss/78766/Share-my-solution
# https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C%2B%2B
# keep going forward until stuck - the reason for stuck is that we hit the exit (end node)
# so we'll find the end node first and delete the path to this node (backtrack)
# then the remaining nodes (flights) form cycles, we could follow any path without stuck 
# until hit the last node in this cycle, this path will be found later, by backtracking
# O(n) to find the route, but O(nlogn) to sort the tickets in order to keep the lexical order
# we can also use min heap to keep this order, also O(nlogn) with heap operations
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = collections.defaultdict(list)
        tickets.sort(reverse = True)
        for frm, to in tickets:
            flights[frm].append(to)

        itn = []

        def fly(start):
            while (flights[start]):
                fly(flights[start].pop())
            itn.append(start)

        fly('JFK')
        return itn[::-1]

# using stack
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = collections.defaultdict(list)
        tickets.sort(reverse = True)
        for frm, to in tickets:
            flights[frm].append(to)
        
        itn = []
        stack = ['JFK'] # the end of stack is the current start
        while stack:
            while flights[stack[-1]]:
                stack.append(flights[stack[-1]].pop())
            itn.append(stack.pop())
        
        return itn[::-1]

# Not good enough, slow as well as takes too much space, though AC
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        avl = collections.defaultdict(int) # record the used tickets, important
        for frm, to in tickets:
            graph[frm].append(to)
            avl[(frm, to)] += 1
        for frm in graph: graph[frm].sort()
        
        def find(itn, start):
            itn.append(start) # must append before check and return True
            if (len(itn) == len(tickets) + 1): return True
            for to in graph[start]:
                if (avl[(start, to)]):
                    avl[(start, to)] -= 1
                    if (find(itn, to)): return True
                    avl[(start, to)] += 1
            itn.pop()
            return False
            
        itn = []
        find(itn, 'JFK')
        return itn
