def bubble_sort(arr):
    """
    Bubble sort algorithm to sort an array in ascending order.
    
    Args:
        arr: List of elements to sort
    
    Returns:
        The sorted list
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps were made, array is already sorted
        if not swapped:
            break
    
    return arr


def bubble_sort_descending(arr):
    """
    Bubble sort algorithm to sort an array in descending order.
    
    Args:
        arr: List of elements to sort
    
    Returns:
        The sorted list in descending order
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:  # Changed comparison for descending
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr


if __name__ == "__main__":
    # Test the bubble sort algorithm
    numbers = [64, 34, 25, 12, 22, 11, 90]
    
    # Test ascending sort
    print("Original array:", numbers.copy())
    sorted_asc = bubble_sort(numbers.copy())
    print("Sorted (ascending):", sorted_asc)  # Output: [11, 12, 22, 25, 34, 64, 90]
    
    # Test descending sort
    sorted_desc = bubble_sort_descending(numbers.copy())
    print("Sorted (descending):", sorted_desc)  # Output: [90, 64, 34, 25, 22, 12, 11]
