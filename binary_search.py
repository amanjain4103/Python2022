
# binary search on a sorted list
def binary_search(given_list: list, sorting_type: str, element_to_search: int) -> int:
    print('binary search')
    lo, hi = 0, len(given_list)-1

    while lo <= hi:
        mid = (lo + hi) // 2
        print(lo, hi, mid)
        if given_list[mid] > element_to_search:
            if sorting_type == 'asc':
                hi = mid - 1
            else:
                lo = mid + 1
        elif given_list[mid] < element_to_search:
            if sorting_type == 'asc':
                lo = mid + 1
            else:
                hi = mid - 1
        else:
            # element found
            return mid
    return -1


# main program body
myAscList = [3, 4, 5, 7, 8, 9, 10]
myDscList = [8, 5, 3, 1, -1, -10]

found_index = binary_search(myAscList, 'asc', 9)
new_found_index = binary_search(myDscList, 'desc', 1)

if found_index == -1:
    print('Element not found')
else:
    print('Element found on index ', found_index)

if new_found_index == -1:
    print('Element not found')
else:
    print('Element found on index ', new_found_index)
