from collections import deque
class Solution:
    def validPath(self, n: int, edges: list[list[int]],
                  source: int, destination: int) -> bool:
            def bfs(graph,start):
                visited = {start}

                queue = deque([start])

                while queue:
                    node = queue.popleft()
                    
                    if node == destination:
                        return True
                    
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                return False
        # 1. Create an empty adjacency list.
            graph = [[] for _ in range(n)]
        # 2. Loop through each edge [u, v].
            for u,v in edges:
        # 3. Add both directions because the graph
        #    is undirected.
                graph[u].append(v)
                graph[v].append(u)

        # Send me your graph-construction code here.
            return bfs(graph,source)

            
        