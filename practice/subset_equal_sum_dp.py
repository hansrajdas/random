def subset_with_equal_sum(A):
    if sum(A) % 2:
        return False
    half_sum = sum(A) // 2
    n = len(A)

    dp = [[None] * (half_sum + 1) for _ in range(n + 1)]

    for element in range(n + 1):
        for _sum in range(half_sum + 1):
            if not element:
                dp[element][_sum] = False
            elif not _sum:
                dp[element][_sum] = True
            elif dp[element - 1][_sum]:
                dp[element][_sum] = dp[element - 1][_sum]
            else:
                if _sum >= A[element - 1]:
                    dp[element][_sum] = dp[element - 1][_sum - A[element - 1]]
    return dp[n][half_sum]



assert subset_with_equal_sum([3, 1, 1, 2, 2, 1]) == True  # 3,1,1 == 2,2,1
assert subset_with_equal_sum([3, 1, 1, 2, 2, 10]) == False
assert subset_with_equal_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]) == True
assert subset_with_equal_sum([1, 2, 3, 4, 5, 6, 7]) == True
assert subset_with_equal_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]) == True
assert subset_with_equal_sum([1, 10, 5, 21, 4]) == False
assert subset_with_equal_sum([1, 10, 5, 21, 4, 1]) == True
