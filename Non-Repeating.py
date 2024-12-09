

# Find the First Non-Repeating Element:

def first_non_repeating(nums):
    from collections import Counter

    # Step 1: Count the frequency of each element
    count = Counter(nums)

    # Step 2: Find the first non-repeating element
    for num in nums:
        if count[num] == 1:
            return num

    return None  # If all elements repeat

# Example usage
nums = [4, 5, 1, 2, 0, 4, 1, 2]
result = first_non_repeating(nums)
print(f"The first non-repeating element is: {result}")


# O(n)
