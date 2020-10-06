def longest_common_subsequence(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    dp = [[None] * (n2 + 1) for _ in range(n1 + 1)]
    
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            if not (i and j):
                dp[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n1][n2]


assert longest_common_subsequence("AGGTAB", "GXTXAYB") == 4
assert longest_common_subsequence("ABCDGH", "AEDFHR") == 3
