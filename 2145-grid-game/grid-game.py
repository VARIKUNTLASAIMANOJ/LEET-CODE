class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        upper_prefix = [0] * n
        lower_prefix = [0] * n

        upper_prefix[0] = grid[0][0]
        lower_prefix[0] = grid[1][0]

        for i in range(1, n):
            upper_prefix[i] = upper_prefix[i - 1] + grid[0][i]
            lower_prefix[i] = lower_prefix[i - 1] + grid[1][i]

        total_upper = upper_prefix[-1]
        total_lower = lower_prefix[-1]
        min_second_robot = float('inf')

        for i in range(n):
            upper_remaining = total_upper - upper_prefix[i]
            lower_remaining = lower_prefix[i - 1] if i > 0 else 0
            second_robot_points = max(upper_remaining, lower_remaining)
            min_second_robot  = min(min_second_robot, second_robot_points)
        
        return min_second_robot