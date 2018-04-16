#Return the index of the number you are searching for

array = []

def create_array(top):
    for i in top:
        array.append(i)

create_array(list(range(90)))

def binary_search(array, number_to_search):
    pivot = int((len(array)/2))
    if number_to_search > array[-1] or number_to_search < array[0]:
        return "Number is not on the list"
    if number_to_search == array[pivot]:
        return True
    if number_to_search < array[pivot]:
        return binary_search(array[:pivot], number_to_search)
    if number_to_search > array[pivot]:
        return binary_search(array[(pivot+1):], number_to_search)
    return False
    
array2 = [3,4,5,6,7]

print(binary_search(array2, 3))
