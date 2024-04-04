def pivot_naive(seq):
    # Honestly you can do almost anything here; heck, just return the last element of seq
    return seq[len(seq)-1]

def partition_naive(seq, pivot):
    left = []
    right = []
    pivots = []
    for i in seq:
        if i > pivot:
            right.append(i)
        elif i < pivot:
            left.append(i)
        else:
            pivots.append(i)
    return [left,pivots,right]

def quicksort_naive(seq):
    if len(seq) <= 1:
        return seq
    pivot = pivot_naive(seq)
    left,right,pivots = partition_naive(seq,pivot)
    answer = quicksort_naive(left) + pivots + quicksort_naive(right)
    list[:] = answer

def pivot_upgrade(seq, lo, hi):
    pass        ### TODO

def quicksort_upgrade(seq):
    __quicksort_upgrade(seq, 0, len(seq))

def __quicksort_upgrade(seq, lo, hi):
    pass        ### TODO

def partition_upgrade(seq, pivot, lo, hi):
    [one, two, three] = partition_naive(seq[lo:hi], pivot)
    seq[lo:hi] = one + two + three
    return [len(one), len(two), len(three)]

def partition_upgrade(seq, pivot, lo, hi):
    pass        ### TODO

tester = [1,6,43,2]
print()