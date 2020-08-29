def solve(A):
    _m = A[0]
    max_idx = 0
    for i in range(len(A)):
        if _m < A[i]:
            max_idx = i
            _m = A[i]
    return ((max_idx + 1) % len(A)) + 1

def main():
    n = input()
    nums = input()
    nums = nums.split()
    nums = [int(n) for n in nums]
    print(solve(nums))

main()
