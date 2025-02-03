from collections import defaultdict


def findRepeatedElem(arr):
    store = defaultdict(int)
    for num in arr:
        store[num] += 1

    print(store)

    for k, v in store.items():
        if v == 1:
            print(k, end=" ")
        if v > 1:
            print(k, end=" ")


arr = [1, 1, 2, 3, 4, 4, 5, 2]

findRepeatedElem(arr)
