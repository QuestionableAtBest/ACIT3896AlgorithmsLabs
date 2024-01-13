def linear_search(needle,haystack):
    for index,i in enumerate(haystack):
        if i == needle:
            return index
    return None

#Function requires that the haystack provided is sorted.
def binary_search(needle,haystack):
    head = len(haystack)
    tail = 0
    # Intialize head and tail pointers to cover the entire range. For example 
    #tail                head || target:3
    # v                   v
    # [1,2,3,4,5,6,7,8,9,10]
    while head - tail != 1:
        # Set midpoint and then check if it matches target
        #tail   midpoint     head
        # v        v           v
        # [1,2,3,4,5,6,7,8,9,10]
        mid_point = (head+tail)//2
        target = haystack[mid_point]
        if needle == target:
            # Number at midpoint index is the number to find. Return index
            return mid_point
        elif needle > target:
            # The target number (needle) is larger than the number at midpoint, therefore we look in the larger range
            # By setting the tail to the current midpoint then calculating a new midpoint
            # tail    mid        head || target:8
            # v        v           v
            # [1,2,3,4,5,6,7,8,9,10]
            # ====================================
            #         tail  mid   head || target:8
            #           v    v     v
            # 1,2,3,4,5,[6,7,8,9,10]
            tail = mid_point + 1
        elif needle < target:
            # Same concept but now the needle is smaller so we shift the head instead
            head = mid_point - 1
    # Last check to handle an edge case not covered in this function
    if needle == haystack[tail]:
        return tail
    return None

# print(linear_search(11,[1,2,3,4,5,6,7,8,10]))
print(binary_search(1,[1,2,3,4,5,6]))

