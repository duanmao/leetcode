class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        # O(VE) where V and E are the number of vertices and edges respectively
        # space: O(V)
        def bellmanford():
            delay = [0] + [float('inf')] * N
            delay[K] = 0
            for i in range(N):
                for u, v, w in times:
                    delay[v] = min(delay[v], delay[u] + w)
            return max(delay) if max(delay) < float('inf') else -1
                
        # Time: O(ElogE), space: O(V)
        def dijkstra():
            
            def buildGraph():
                graph = collections.defaultdict(list)
                for out, iin, cost in times:
                    graph[out].append((iin, cost))
                return graph

            graph = buildGraph()
            heap = [(0, K)]
            arrived = {}
            while (heap):
                curcost, node = heapq.heappop(heap)
                if (node not in arrived):
                    arrived[node] = curcost
                    for v, cost in graph[node]:
                        heapq.heappush(heap, (curcost + cost, v))
            return max(arrived.values()) if len(arrived) == N else -1
        
        return dijkstra()
