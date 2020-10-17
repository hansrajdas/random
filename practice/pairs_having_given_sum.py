def pairs_having_given_sum(A, x):
   m = {}
   for k in A:
    if k in m:
        m[k] += 1
    else:
        m[k] = 1

    for k in m:
        required = x - k
        if required == k:
            if m[k] > 1:
                print(k, k)
                m[k] -= 2
        else:
            if required in m and m[required] > 0 and m[k] > 0:
                print(k, required)
                m[k] -= 1
                m[required] -= 1


pairs_having_given_sum([1,2,3,4,2,3,2,2], 4)
