# https://leetcode.com/problems/redundant-connection-ii/discuss/141897/3ms-Union-Find-with-Explanations
# union-find
# O(n)
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        
        def find(x):
            if (x not in parent): parent[x] = x
            if (parent[x] != x):
                parent[x] = find(parent[x])
            return parent[x]
            
        twoparents = cyclelink = None
        for edge in edges:
            prt, child = edge
            childroot, parentroot = find(child), find(prt)
            if (childroot != child): # this child has more than one parent
                twoparents = edge
            elif (childroot == parentroot): # found a cycle
                cyclelink = edge
            else: # union
                parent[childroot] = parentroot
        if (not twoparents or not cyclelink):
            print(twoparents, cyclelink)
            return twoparents or cyclelink
        else:
            # we did union for the first double-parented edge, 
            # and skipped the union operation for the second double-parented edge.
            # by skipping the union operation, we essentially mean that 
            # the second edge has been removed by us from the graph.
            # However, after the edge has been removed, there's still a cycle remained in the "tree",
            # which indicates that we have made the wrong choice - we have chosen the wrong edge to remove.
            # that is, we should have removed the first double-parented edge instead.
            for edge in edges:
                if (twoparents[1] == edge[1]): return edge
        return None
