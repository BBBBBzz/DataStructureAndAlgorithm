"""
问题：
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串

示例：
输入：s = "aab" p = "c*a*b"
输出：true
解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        1. if s[i] == p[j] or p[j] == '.': dp[i][j] = dp[i-1][j-1]
        2. if p[j] == '*':
            if p[j-1] != s[i] and p[j-1] != '.': dp[i][j] = dp[i][j-2] # cancel the previous one
            elif p[j-1] == s[i] or p[j-1] == '.': dp[i][j] = dp[i][j-1] or dp[i][j-2] or dp[i-1][j]
        """
        s = ' ' + s
        p = ' ' + p
        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        # 都为空字符串的时候符合条件
        dp[0][0] = True
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == '.': dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if p[j-2] != s[i-1] and p[j-2] != '.': dp[i][j] = dp[i][j-2]
                    else:
                        # a* counts as multiple of a
                        # a* counts as a single a
                        # a* counts as empty\
                        dp[i][j] = dp[i-1][j] or dp[i][j-1] or dp[i][j-2]
        return dp[-1][-1]
