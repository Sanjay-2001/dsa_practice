def removeDuplicate(arr, N):
    i = 0
    for j in range(1, N):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]

    return (arr[:i+1])


arr = [1, 2, 2, 2, 3]
N = len(arr)

print(removeDuplicate(arr, N))
