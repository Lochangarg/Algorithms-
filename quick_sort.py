def quick_sort(arr):
    """
    Quick sort algorithm to sort an array in ascending order.
    Uses divide and conquer approach with pivot element.
    
    Args:
        arr: List of elements to sort
    
    Returns:
        The sorted list
    """
    if len(arr) <= 1:
        return arr
    
    # Choose the middle element as pivot
    pivot = arr[len(arr) // 2]
    
    # Partition into three lists
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort and combine
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr, low, high):
    """
    In-place quick sort implementation.
    
    Args:
        arr: List of elements to sort
        low: Starting index
        high: Ending index
    
    Returns:
        The sorted list
    """
    if low < high:
        # Partition and get pivot index
        pivot_index = partition(arr, low, high)
        
        # Recursively sort left and right partitions
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)
    
    return arr


def partition(arr, low, high):
    """
    Partition helper function for in-place quick sort.
    """
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def get_user_input():
    """
    Get array input from user via command line.
    """
    try:
        user_input = input("Enter numbers separated by spaces: ")
        numbers = list(map(int, user_input.split()))
        return numbers
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return None


if __name__ == "__main__":
    print("=== Quick Sort Algorithm ===\n")
    
    # Get input from user
    arr = get_user_input()
    
    if arr is not None:
        print(f"\nOriginal array: {arr}")
        
        # Method 1: Simple quick sort
        sorted_arr = quick_sort(arr.copy())
        print(f"Sorted (simple quick sort): {sorted_arr}")
        
        # Method 2: In-place quick sort
        arr_copy = arr.copy()
        quick_sort_inplace(arr_copy, 0, len(arr_copy) - 1)
        print(f"Sorted (in-place quick sort): {arr_copy}")
