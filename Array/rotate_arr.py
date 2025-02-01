def rotateArr(arr, k):
    n = len(arr)
    k = k % n
    print(arr[-k:] + arr[:-k])  # right rotation
    print(arr[k:] + arr[:k])  # left rotation


arr = [1, 2, 3, 4, 5]
k = 2

rotateArr(arr, k)
