def quick_sort(lst):
    # Base case: if the list is empty or has one element, it's already sorted
    if len(lst) <= 1:
        return lst[:]
    
    # Choose the last element as the pivot
    pivot = lst[-1]
    
    # Partition the list into three sublists
    less = []
    equal = []
    greater = []
    
    for item in lst:
        if item < pivot:
            less.append(item)
        elif item == pivot:
            equal.append(item)
        else:
            greater.append(item)
    
    # Recursively sort the less and greater sublists
    sorted_less = quick_sort(less)
    sorted_greater = quick_sort(greater)
    
    # Concatenate the sorted lists and the equal list
    return sorted_less + equal + sorted_greater
