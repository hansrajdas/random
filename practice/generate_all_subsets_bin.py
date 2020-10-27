def get_subset(a, i):
    subset = set()
    element_idx = 0
    while i:
        if i & 1:
            subset.add(a[element_idx])
        i >>= 1
        element_idx += 1
    return subset

def generateAllSubsets(a, n):
    idx = 0
    sets = []
    while idx < (1 << n):
        sets.append(get_subset(a, idx))
        idx += 1
    return sets

def main():
  a = []
  n = int(input("Enter number of elements: "))
  for i in range(n):
      x = input("Enter value of a[%d] : " % i)
      a.append(x)

  subsets = generateAllSubsets(a, n)
  print("\nAll subsets are: ")
  for i in range(len(subsets)):
    print("{idx}: {subset}".format(idx=i, subset=subsets[i]))

if __name__ == '__main__':
  main()

# Output:
# *************************
# python generate_all_subsets.py 
# Enter number of elements: 2
# Enter value of a[0] : 1
# Enter value of a[1] : 2
# 
# All subsets are: 
# 0: set([])
# 1: set([1])
# 2: set([2])
# 3: set([1, 2])
#
# python generate_all_subsets.py 
# Enter number of elements: 3
# Enter value of a[0] : 1
# Enter value of a[1] : 2
# Enter value of a[2] : 3
# 
# All subsets are: 
# 0: set([])
# 1: set([1])
# 2: set([2])
# 3: set([1, 2])
# 4: set([3])
# 5: set([1, 3])
# 6: set([2, 3])
# 7: set([1, 2, 3])


