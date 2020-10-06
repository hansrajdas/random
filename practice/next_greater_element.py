def print_next_greater_element(A):
    stack = []
    nge = [-1 for _ in range(len(A))]

    for i in range(len(A) - 1, -1, -1):
        while stack and stack[-1] < A[i]:
            stack.pop()

        if stack:
            nge[i] = stack.pop()
        else:
            nge[i] = -1

        stack.append(A[i])

    print('NGE: ')
    for i in range(len(A)):
        print('%d -> %d' % (A[i], nge[i]))

print_next_greater_element([11, 13, 21, 3])
# 11 -> 13
# 13 -> 21
# 21 -> -1
# 3 -> -1

print_next_greater_element([11, 13, 14, 15, 20])
# 11 -> 13
# 13 -> 14
# 14 -> 15
# 15 -> 20
# 20 -> -1

print_next_greater_element([5, 4, 3, 2, 1])
# 5 -> -1
# 4 -> -1
# 3 -> -1
# 2 -> -1
# 1 -> -1

print_next_greater_element([11, 15, 10, 12, 13])
# 11 -> 15
# 15 -> -1
# 10 -> 12
# 12 -> 13
# 13 -> -1
