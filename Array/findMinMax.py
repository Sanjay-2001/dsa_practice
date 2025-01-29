def getMinMax(arr):
    minElement = float('inf')
    maxElement = float('-inf')

    for i in range(len(arr)):
        minElement = min(minElement, arr[i])
        maxElement = max(maxElement, arr[i])

    return minElement, maxElement


arr = [1, 4, 2, 5, 7]

print(getMinMax(arr))
