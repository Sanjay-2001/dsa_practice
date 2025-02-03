def findSymetricPair(arr, N):
    store = {}
    for nums in arr:

        first, second = nums

        if second in store and store[second] == first:
            print(f"({first}, {second})", end=" ")

        store[first] = second


arr = [[1, 2], [2, 1], [3, 4], [4, 5], [5, 4]]
N = len(arr)

findSymetricPair(arr, N)
