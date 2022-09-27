# linear search
def linear_search(given_list, element_to_search):
    for index in range(0, len(given_list)-1):
        if given_list[index] == element_to_search:
            return index
    return -1

# main program body
myList = [1, 4, 5, 12, 55, 67, 90]
element_to_find = int(input('Enter Element to find '))
found_index = linear_search(myList, element_to_find)
if found_index == -1:
    print('Element does not Exists!')
else:
    print('Element Found on Index ', found_index)
