import sys

def search_element(arr, element) -> int:
    left_index = 0
    right_index = len(arr) - 1
    print("-----")
    while left_index <= right_index:
        mid = (right_index + left_index)//2
        if element == arr[mid]:
            return mid
        elif element < arr[mid]:
            right_index = mid - 1
        elif element > arr[mid]:
            left_index = mid + 1
        # print(left_index, mid, right_index)

    
    return -1



def main():
    element = int(sys.argv[1])
    print(element)
    arr = [2,4,5,6,8,9,12]
    for a in arr:
        print(search_element(arr, a))

    # print(search_element(arr, element))
    

if __name__ == "__main__":
    main()
