class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        color = {}
        components = []
        def is_bipartite(start):
            """Check if a component is bipartite and return its nodes."""
            queue = deque([start])
            color[start] = 0
            component_nodes = [start]
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[node]  
                        queue.append(neighbor)
                        component_nodes.append(neighbor)
                    elif color[neighbor] == color[node]:  
                        return False, []
            return True, component_nodes
        for node in range(1, n + 1):
            if node not in color:
                bipartite, component = is_bipartite(node)
                if not bipartite:
                    return -1  
                components.append(component)
        def max_bfs_depth(start):
            """Returns the maximum BFS level in a component starting from node `start`."""
            queue = deque([start])
            visited = set([start])
            level = 0
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                level += 1
            return level
        max_groups = 0
        for component in components:
            max_depth = 0
            for node in component:
                max_depth = max(max_depth, max_bfs_depth(node))
            max_groups += max_depth  
        return max_groups