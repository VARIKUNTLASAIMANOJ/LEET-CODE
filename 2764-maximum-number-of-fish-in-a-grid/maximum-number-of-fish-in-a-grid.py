class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def bfs(r, c):
            queue = deque([(r, c)])
            fish = 0            
            while queue:
                x, y = queue.popleft()
                if grid[x][y] == 0:  
                    continue
                fish += grid[x][y]
                grid[x][y] = 0  
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                        queue.append((nx, ny))
            return fish
        max_fish = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:  
                    max_fish = max(max_fish, bfs(i, j))
        return max_fish