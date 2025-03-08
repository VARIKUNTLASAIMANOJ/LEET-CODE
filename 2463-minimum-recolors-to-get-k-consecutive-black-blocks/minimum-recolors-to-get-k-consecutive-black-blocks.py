class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_recolors = float('inf')
        white_count = blocks[:k].count('W')
        min_recolors = white_count
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                white_count -= 1
            if blocks[i] == 'W':
                white_count += 1
            min_recolors = min(min_recolors, white_count)
        return min_recolors