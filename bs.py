
def bs(num, target):
    left = 0
    right = len(num) - 1

    while left <= right:
        mid = (left + right)//2

        if num[mid] == target:
            return (mid)
        elif num[mid] > target:
            right = mid -1
        else:
            left = mid + 1

    return (-1)


def 
