def findEquilibrium(arr, N):
    total = sum(arr)
    left, right = 0, total
    for i in range(N):
        right -= arr[i]
        if left == right:
            return i
        left += arr[i]

    return -1


nums = [2, 3, -1, 8, 4]
n = len(nums)
print(findEquilibrium(nums, n))
