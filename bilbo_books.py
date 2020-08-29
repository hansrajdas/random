def solve(A):
    _d = {}
    for i in A:
        if i in _d:
            _d[i] += 1
        else:
            _d[i] = 1
    return min(_d[k] for k in _d)


def main():
    n = int(input())
    nums = input()
    nums = nums.split()
    nums = [int(i) for i in nums]
    print(solve(nums))

main()
# print(solve([2, 4, 2, 4, 3, 2, 3]))
# print(solve([1, 2]))
