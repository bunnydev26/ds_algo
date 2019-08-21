import sys

def search_element(arr, element, left_index, right_index) -> int:
    if left_index > right_index:
        return -1
    mid = (right_index + left_index) // 2
    if element == arr[mid]:
        return mid
    elif element < arr[mid]:
        return search_element(arr, element, left_index, right_index - 1)

    return search_element(arr, element, left_index + 1 , right_index)

def main():
    element = int(sys.argv[1])
    arr = [2,4,5,6,8,9,12]
    # for a in arr:
    #     print(search_element(arr, a))

    print(search_element(arr, element, 0 , len(arr)-1))
    

if __name__ == "__main__":
    main()
