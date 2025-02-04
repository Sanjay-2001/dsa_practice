def binary_search(arr, k):
    low = 0
    high = len(arr)-1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > k:
            high = mid-1

        elif arr[mid] < k:
            low = mid + 1
        else:
            ans = mid
            break

    return ans


arr = [3, 5, 6, 7, 9, 10]
k = 10
result = binary_search(arr, k)
print(result)
