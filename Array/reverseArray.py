def getReverseArray(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


arr = [1, 5, 3, 4, 2, 6]
print("reverse array : ", getReverseArray(arr))


# arr.reverse()
