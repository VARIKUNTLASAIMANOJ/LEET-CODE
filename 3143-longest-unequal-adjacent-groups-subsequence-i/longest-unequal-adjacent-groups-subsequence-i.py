class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = []
        prev_group = -1
        for word, group in zip(words, groups):
            if group != prev_group:
                result.append(word)
                prev_group = group
        return result