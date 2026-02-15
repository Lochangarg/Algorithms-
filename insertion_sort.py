def insertion_sort(arr):
    """
    Insertion sort algorithm to sort an array in ascending order.
    Builds the sorted array one item at a time by inserting elements 
    into their correct position.
    
    Args:
        arr: List of elements to sort
    
    Returns:
        The sorted list
    """
    # Start from the second element (index 1)
    for i in range(1, len(arr)):
        key = arr[i]  # Element to be inserted
        j = i - 1  # Index of the last element in sorted portion
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key at its correct position
        arr[j + 1] = key
    
    return arr


def insertion_sort_descending(arr):
    """
    Insertion sort algorithm to sort an array in descending order.
    
    Args:
        arr: List of elements to sort
    
    Returns:
        The sorted list in descending order
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Compare for descending order
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr


if __name__ == "__main__":
    # Test the insertion sort algorithm
    numbers = [64, 34, 25, 12, 22, 11, 90]
    
    # Test ascending sort
    print("Original array:", numbers.copy())
    sorted_asc = insertion_sort(numbers.copy())
    print("Sorted (ascending):", sorted_asc)  # Output: [11, 12, 22, 25, 34, 64, 90]
    
    # Test descending sort
    sorted_desc = insertion_sort_descending(numbers.copy())
    print("Sorted (descending):", sorted_desc)  # Output: [90, 64, 34, 25, 22, 12, 11]
    
    # Test with already sorted array
    sorted_array = [1, 2, 3, 4, 5]
    print("\nAlready sorted array:", sorted_array)
    print("After insertion sort:", insertion_sort(sorted_array.copy()))
