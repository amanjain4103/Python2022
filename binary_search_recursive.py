# binary search with recursive approach // for time saving we are expecting list to be in ascending order
def binary_search(given_list: list, lo: int, hi: int, element_to_search: int) -> int:
    if lo <= hi:
        mid = (lo + hi) // 2
        if given_list[mid] < element_to_search:
            return binary_search(given_list, mid + 1, hi, element_to_search)
        elif given_list[mid] > element_to_search:
            return binary_search(given_list, lo, mid - 1, element_to_search)
        else:
            return mid
    else:
        return -1


# main program flow
myList = [1, 2, 4, 5, 6, 7, 8, 9]
found_index = binary_search(myList, 0, len(myList)-1, 8)

if found_index == -1:
    print('Element not found')
else:
    print('Element found at index ', found_index)
