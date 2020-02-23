# https://leetcode.com/problems/word-break/
# Medium

# First iteration exceeded time. Trying now to reduce the wordDict size
# Second iteration exceeded time. Some wordDicts are too long
# Final: Use DP. Need to practice this more
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        N = len(s)
        dp = [0] * (N + 1)
        dp[0] = 1
        start_indexes = [0]
        
        for i in range(1, N+1):
            for start_idx in start_indexes:
                word = s[start_idx:i]
                if word in wordDict:
                    dp[i] = 1
                    start_indexes.append(i)
                    break
        return bool(dp[N])