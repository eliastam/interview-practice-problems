def compare_arrays(l1, l2):
    x = 0
    y = 0
    min_len = min([len(l1), len(l2)])
    for i in range(0, min_len):
        x = l1[i]
        y = l2[i]
        if x > y :
            return l1
        elif y > x :
            return l2
    return l1

def contiguous_subarray (l, k):
    A = [-1]
    B = []
    length = len(l)
    index = 0
    while index + k <= length :
        B = l[index: index+k]
        A = compare_arrays(A, B)
        index +=1
    print(A)

l = [1,4,3,2,5,6,7,7,9,11,12]
contiguous_subarray (l, 4)