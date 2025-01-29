# def numOfOccurence(arr):

#     arr.sort()

#     valueDict = {}

#     for num in arr:
#         if num in valueDict:
#             valueDict[num] += 1
#         else:
#             valueDict[num] = 1

#     return valueDict


# arr = [10, 5, 10, 15, 10, 5]
# print(numOfOccurence(arr))


from collections import defaultdict


def getFreq(arr):
    store = defaultdict(int)
    for num in arr:
        store[num] += 1

    for key, val in store.items():
        print(key, val)


getFreq([10, 5, 10, 15, 10, 5])
