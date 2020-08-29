def solve(A):
    A.sort(reverse=True)
    res = 0
    i = 0
    while i < len(A):
        res += A[i]
        if i < len(A) - 1 and A[i] - 1 == A[i + 1]:
            i += 1
        i += 1
    return res

def main():
    nums = input()
    nums = nums.split()
    nums = [int(n) for n in nums]
    print(solve(nums))

main()
