class Solution:
    # The state of the game can be represented as (m, c, t) 
    # where m is the location of the mouse, 
    # c is the location of the cat, 
    # and t is 1 if it is the mouse's move, else 2. 
    # Let's call these states nodes. 
    # These states form a directed graph: the player whose turn it is 
    # has various moves which can be considered as outgoing edges from this node to other nodes.

    # Some of these nodes are already resolved: 
    # if the mouse is at the hole (m = 0), then the mouse wins; 
    # if the cat is where the mouse is (c = m), then the cat wins. 
    # So nodes will either be colored MOUSE, CAT, or DRAW depending on which player is assured victory.
    
    # We will color each node marked DRAW according to the following rule. 
    # (We'll suppose the node has node.turn = Mouse: the other case is similar.)

    # * "Immediate coloring": 
    # If there is a child that is colored MOUSE, which means mouse will win from this child node,
    # then its parent node should also be colored MOUSE.

    # * "Eventual coloring": 
    # If all children are colored CAT, namely there's no way for mouse to win from the parent node,
    # then this parent node will be colored CAT.

    # We will repeatedly do this kind of coloring until no node satisfies the above conditions. 
    # To perform this coloring efficiently, we will use a queue and perform a bottom-up percolation:

    # Enqueue any node initially colored (because the Mouse is at the Hole, or the Cat is at the Mouse.)
    # For every node in the queue, for each parent of that node:
    # 1) Try to do an immediate coloring of parent if you can.
    # 2) If you can't, then decrement the side-count of the number of children marked DRAW. 
    #    If it becomes zero, then do an "eventual coloring" of this parent.
    # All parents that were colored in this manner get enqueued to the queue.
    
    def catMouseGame(self, graph: List[List[int]]) -> int:
        N = len(graph)

        # What nodes could play their turn to
        # arrive at node (m, c, t) ?
        def parents(m, c, t):
            if t == 2:
                # currently it's cat's turn
                # parents should be mouse's turn
                for m2 in graph[m]:
                    yield m2, c, 3-t
            else:
                for c2 in graph[c]:
                    if c2:
                        yield m, c2, 3-t

        DRAW, MOUSE, CAT = 0, 1, 2
        color = collections.defaultdict(int)

        # degree[node] : the number of neutral children of this node
        degree = {}
        for m in range(N):
            for c in range(N):
                degree[m,c,1] = len(graph[m])
                degree[m,c,2] = len(graph[c]) - (0 in graph[c])

        # enqueued : all nodes that are colored
        queue = collections.deque([])
        for i in range(N):
            for t in range(1, 3):
                # mouse at 0 (hole), mouse wins
                color[0, i, t] = MOUSE
                queue.append((0, i, t, MOUSE))
                # cat cannot be at hole
                if i > 0:
                    # cat and mouse are at the same node, cat wins
                    color[i, i, t] = CAT
                    queue.append((i, i, t, CAT))

        # percolate
        while queue:
            # for nodes that are colored :
            i, j, t, c = queue.popleft()
            # for every parent of this node i, j, t :
            for i2, j2, t2 in parents(i, j, t):
                # if this parent is not colored :
                if color[i2, j2, t2] is DRAW:
                    # if the parent can make a winning move (ie. mouse to MOUSE), do so
                    if t2 == c: # winning move
                        color[i2, j2, t2] = c
                        queue.append((i2, j2, t2, c))
                    # else, this parent will lead to a losing move
                    # so it has degree[parent]--, and enqueue if all children
                    # of this parent are colored as losing moves
                    else:
                        degree[i2, j2, t2] -= 1
                        if degree[i2, j2, t2] == 0:
                            color[i2, j2, t2] = 3 - t2
                            queue.append((i2, j2, t2, 3 - t2))

        return color[1, 2, 1]
