def solve(A):
    local_max = float('-Inf')
    i = len(A) - 1
    while i >=0:
        if A[i] > local_max:
            print(A[i])
        local_max = max(local_max, A[i])
        i -= 1

solve([1,2,3,4])
solve([10, 5, 4, 3, 1])
