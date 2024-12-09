def rotate_array(arr, k):
    """
    Rotates an array k times to the right.
    
    :param arr: List of elements to rotate.
    :param k: Number of times to rotate the array.
    :return: Rotated array.
    """
    if not arr or k <= 0:
        return arr

    n = len(arr)
    k %= n  # Handle cases where k is greater than array length.
    return arr[-k:] + arr[:-k]

# Example usage
array = [1, 2, 3, 4, 5]
rotations = 2
rotated_array = rotate_array(array, rotations)
print("Original array:", array)
print("Rotated array:", rotated_array)
