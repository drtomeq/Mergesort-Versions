the_list =[4,8,2,8,43,9,17,25,2,0,6,3]


"""Mergesort program by using list indices

While it doesn't follow the 'divide and conquer' algorithm as
litterally as mergesort_with_lists
We save resources by not creating new lists each time
This version is in-place, 
that is we do not extend the memory requirements beyond the list
but in doing so may need several more swaps"""

def half_and_sort(start, end):
    """ Splits the list into 2 and combines them sorted

    The recursion of mergesort is seen in this function
    To stop an infinite loop terminate the halving process 
    when empty or just a single element
    """
    if end>start:
        split_position = (start + end) // 2
        mergesort(start,split_position,end)

def combine_two_lists(start=0, split=len(the_list)//2, end=len(the_list)):
    """ Sorts elements between start and end positions 
    
    It does this by splitting into two lists 
    start to split and split +1 to end 
    Assumes that two lists are themselves ordered
    This is a fair assumption if mergesort algorithm works right
    It uses a version of insertion sort 
    Not the most time efficient, but keeps it in-place"""

    # if 1 list is empty, no need to change anything
    if start>split or split>end:
        return
    # pos2_start = split+1 # position in list 2
    for pos2_start in range(split+1,end+1):
        pos2 = pos2_start
        # keep moving element from list 2 left
        # until it is no longer greater than the previous element
        while the_list[pos2] < the_list[pos2-1] and pos2>0:
            # swap
            the_list[pos2], the_list[pos2-1] = the_list[pos2-1], the_list[pos2]
            pos2 -= 1

def mergesort(start=0, split=(len(the_list)-1)//2, end=len(the_list)-1):
    """Sort by halving list into 2 sublists and combining sorted
    
    The algorithm is inheritly recursive as sorting calls mergesort
    The idea is we keep on halfing each sublist until they can no longer be halved
    This is when they are either empty or have a single element
    We then combine the half elements sorted"""
    
    if split>start:
        split_position = (start + split) // 2
        mergesort(start,split_position,split)

    if end>start:
        split_position = (split+1 + end) // 2
        mergesort(split+1,split_position,end)


    # half_and_sort(start,split)
    # half_and_sort(split+1,end)

    combine_two_lists(start, split, end)

print(mergesort())
print(the_list)