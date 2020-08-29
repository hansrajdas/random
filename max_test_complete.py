def max_test_complete(A):
    _m = -1
    max_idx = -1
    for i in range(len(A)):
        if _m < A[i] and A[i] < len(A):
            max_idx = i
            _m = A[i]
    return ((max_idx + 1) % len(A)) + 1

def main():
    n = input()
    extra_time = input()
    extra_time = extra_time.split()
    extra_time = [int(n) for n in extra_time]
    print(max_test_complete(extra_time))

main()
