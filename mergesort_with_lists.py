"""Mergesort program by splitting larger lists into 2 smaller lists

Perhaps not the most resource friendly way of doing it,
but it follows the 'divide and conquer' algorithm more literally"""

def half_and_sort(whole_list):
    """ Splits the list into 2 and combines them sorted

    The recursion of mergesort is seen in this function
    To stop an infinite loop terminate the halving process 
    when empty or just a single element
    """
    if len(whole_list)>1:
        split_position = len(whole_list)//2
        left = whole_list[:split_position]
        right =whole_list[split_position:]
        whole_list = mergesort(left,right)
    return whole_list

def combine_two_lists(list1:list , list2:list):
    """ Returns a single ordered list with elements from list1 and list 2 
    
    Assumes that list1 and list2 are themselves ordered
    This is a fair assumption if mergesort algorithm works right"""
    # if 1 list is empty, the combined list is simply the other
    if len(list1) <1:
        return list2
    if len(list2) <1:
        return list1

    pos1 = 0 # position in list 1
    pos2 = 0 # position in list 2
    while pos1 < len(list1):
        # keep inserting elements in list 2 
        # until they are greater than that in list1
        while list2[pos2] < list1[pos1]:
            list1.insert(pos1, list2[pos2])
            pos2 += 1
            # if we have inserted all elements in list2 
            # we are done
            if pos2 >= len(list2):
                return list1
            # as we have inserted an element into list1
            # we have to move one place onwards to get same one
            pos1 += 1
        pos1 += 1
    # if we have any remaining elements in list2, add to end of list1
    list1.extend(list2[pos2:])
    return list1
            

def mergesort(left, right=[]):
    """Sort by halving list into 2 sublists and combining sorted
    
    The algorithm is inheritly recursive as sorting calls mergesort
    The idea is we keep on halfing each sublist until they can no longer be halved
    This is when they are either empty or have a single element
    We then combine the half elements sorted"""
    left=half_and_sort(left)
    right=half_and_sort(right)
    return combine_two_lists(left, right)

print(mergesort([4,8,2,8,43,9,4,8,32,7,2,6,2,8,2]))