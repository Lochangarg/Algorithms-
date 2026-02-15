def linear_search(arr, target):
    """
    Linear search algorithm to find a target value in an array.
    
    Args:
        arr: List of elements to search through
        target: The value to search for
    
    Returns:
        The index of the target if found, otherwise -1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def linear_search_all(arr, target):
    """
    Linear search variant that returns all indices where target appears.
    
    Args:
        arr: List of elements to search through
        target: The value to search for
    
    Returns:
        List of indices where target is found, empty list if not found
    """
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices


if __name__ == "__main__":
    # Test the linear search algorithm
    numbers = [10, 25, 3, 47, 12, 8, 33, 25]
    
    # Test single search
    print("Array:", numbers)
    print("Search for 47:", linear_search(numbers, 47))  # Output: 3
    print("Search for 100:", linear_search(numbers, 100))  # Output: -1
    
    # Test multiple occurrences
    print("\nSearch for all 25:", linear_search_all(numbers, 25))  # Output: [1, 7]
