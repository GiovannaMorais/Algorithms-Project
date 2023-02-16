def is_anagram(first_string, second_string):
    firstLower = list(first_string.lower())
    secondLower = list(second_string.lower())

    sorted_first =  quick_sort(firstLower)
    sorted_second = quick_sort(secondLower)

    joinOrderedLetterFirstString = ''.join(sorted_first)
    joinOrderedLetterSecondString = ''.join(sorted_second)

    if first_string == "" or second_string == "":
        return (joinOrderedLetterFirstString, joinOrderedLetterSecondString, False)
    if joinOrderedLetterFirstString != joinOrderedLetterSecondString:
        return (joinOrderedLetterFirstString, joinOrderedLetterSecondString, False)

    return (joinOrderedLetterFirstString, joinOrderedLetterSecondString, True)


def quick_sort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
        
    if start < end:
        p = partition(array, start, end) 
        quick_sort(array, start, p - 1)
        quick_sort(array, p + 1, end) 
    return array

def partition(array, start, end):
    pivot = array[end]
    delimiter = start - 1

    for index in range(start, end):
        if array[index] <= pivot:
          delimiter = delimiter + 1
          array[index], array[delimiter] = array[delimiter], array[index]

    array[delimiter + 1], array[end] = array[end], array[delimiter + 1]
    return delimiter + 1
