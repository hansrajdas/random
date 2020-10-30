def merge(A, len_a, B, len_b):
    if not B:
        return
    b_idx = len_b - 1
    a_idx = len_a - 1
    idx = len(A) - 1

    while b_idx >= 0:
        if a_idx >=0 and A[a_idx] > B[b_idx]:
            A[idx] = A[a_idx]
            a_idx -= 1
        else:
            A[idx] = B[b_idx]
            b_idx -= 1
        idx -= 1


def main():
    # Case 1:
    B = [1, 2, 3]
    A = [4, 5, 6, 7] + [None] * len(B)
    merge(A, 4, B, 3)
    print(A)

    # Case 2:
    B = [8, 9, 10]
    A = [4, 5, 6, 7] + [None] * len(B)
    merge(A, 4, B, 3)
    print(A)


main()
