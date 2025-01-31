class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        island_id = 2 
        island_sizes = {0: 0}  
        def dfs(r, c, id):
            stack = [(r, c)]
            size = 0
            while stack:
                x, y = stack.pop()
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = id  
                    size += 1
                    for dx, dy in directions:
                        stack.append((x + dx, y + dy))
            return size
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_sizes[island_id] = dfs(r, c, island_id)
                    island_id += 1  
        max_island = max(island_sizes.values()) 
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:  
                    unique_islands = set()
                    for dx, dy in directions:
                        nr, nc = r + dx, c + dy
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            unique_islands.add(grid[nr][nc])
                    new_size = 1 + sum(island_sizes[i] for i in unique_islands)
                    max_island = max(max_island, new_size)
        return max_island