# Juggling algorithm
# Program for array rotation
# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements

def gcd(num1, num2):
    if(num2 == 0):
        return num1
    return gcd(num2, num1%num2)

def leftRotate(arr, n, d):
    g_c_d = gcd(n, d)
    for curr_set_index in range(g_c_d):
        
        # We save the first element of the first set
        first_element = arr[curr_set_index]
        # We mark the last index in set as the current index
        last_index_in_set = curr_set_index

        # infinte loop
        while True:
            # we calculate the next index in set by adding the last pointing index and the next element
            next_index_in_set = last_index_in_set + d
            # if the next index is great than the total element in the array
            if next_index_in_set >= n:
                # we make sure it points to the begining
                next_index_in_set = next_index_in_set - n
            if next_index_in_set == curr_set_index:
                # we reached back to the index of the set we started from
                break
            # me move the element from the next set to the last set
            arr[last_index_in_set] = arr[next_index_in_set]
            # we move the last index to the next index
            last_index_in_set = next_index_in_set
        arr[last_index_in_set] = first_element


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    d = 4
    n = len(arr)
    print(arr)
    leftRotate(arr, n, d)
    print(arr)

if __name__ == "__main__":
    main()