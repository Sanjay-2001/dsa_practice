from collections import Counter


def getSortByFreqn(arr):
    freq = Counter(arr)

    arr.sort(key=lambda x: (-freq[x], x))

    return arr


# Test case
arr = [1, 2, 3, 2, 4, 3, 1, 2]
sorted_arr = getSortByFreqn(arr)
print(sorted_arr)
