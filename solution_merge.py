# Lab 12 Merge Sort: https://gist.github.com/jholman-bcit/5fdc23ced4ee910b3242632f54d55168
def cheat_sort(seq):
    seq.sort()

def cheat_merge(left, right):
    return sorted(left + right)

# def merge(left,right):
#     # Initialize the index of left and right (i and j respectively, yes i could use more specific names, no i won't be doing that.)
#     i = 0
#     j = 0
#     ans = []
#     # While either one still has numbers, compare which ones is smaller
#     while i < len(left) and j < len(right):
#         #Case where left is smaller, put it in ans list then increment left to next number
#         if left[i] < right[j]:
#             ans.append(left[i])
#             i += 1
#         #Case where right is smaller, same thing
#         else:
#             ans.append(right[j])
#             j += 1
    
#     #Two while loops at the end to add the remaining numbers not compared, because one of the lists is now "finished", we know the rest of numbers in the remaining list are all larger and sorted.
#     while i < len(left):
#         ans.append(left[i])
#         i += 1

#     while j < len(right):
#         ans.append(right[j])
#         j += 1

#     return ans

# def merge_sort(seq):
#     if len(seq) <= 1:
#         return seq
#     else:
#         midpoint = len(seq)//2
#         left = seq[:midpoint]
#         right = seq[midpoint:]
#         sorted_l = merge_sort(left)
#         sorted_r = merge_sort(right)
#         return merge(sorted_l,sorted_r)

def merge(left, right, seq):
    # Initialize the index of left and right (i and j respectively, yes i could use more specific names, no i won't be doing that.)
    i = 0
    j = 0
    # instead of a a"nswer" list we now use an extra index here to keep track of where we are in seq
    k = 0

    # While either one still has numbers, compare which ones is smaller
    while i < len(left) and j < len(right):
        # Decide which number to put in seq
        if left[i] < right[j]:
            #Case where left is smaller, increment left to next number
            seq[k] = left[i]
            i += 1
        else:
            #Right case
            seq[k] = right[j]
            j += 1
        # Have to increment k in both scenarios so put here
        k += 1
    
    #Cases to handle the remaining numbers left in the list thats not finished
    while i < len(left):
        seq[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        seq[k] = right[j]
        j += 1
        k += 1

def merge_sort(seq):
    if len(seq) <= 1:
        return
    else:
        midpoint = len(seq) // 2
        left = seq[:midpoint]
        right = seq[midpoint:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, seq)