class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        def is_valid(start: int) -> bool:
            original = [0] * n
            original[0] = start
            for i in range(1, n):
                original[i] = original[i - 1] ^ derived[i - 1]
            return (original[0] ^ original[n - 1]) == derived[n - 1]
        return is_valid(0)