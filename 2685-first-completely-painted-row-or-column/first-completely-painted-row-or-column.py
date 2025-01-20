class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        value_to_position = {}
        for r in range(m):
            for c in range(n):
                value_to_position[mat[r][c]] = (r, c)
        rows = [0] * m
        cols = [0] * n
        for i, val in enumerate(arr):
            r, c = value_to_position[val]
            rows[r] += 1
            cols[c] += 1
            if rows[r] == n or cols[c] == m:
                return i 
        return -1