# def getHFDF(arr):
#     arr.sort()
#     lengthArr = len(arr)
#     right = lengthArr - 1
#     left = lengthArr//2

#     while left < right:
#         arr[left], arr[right] = arr[right], arr[left]
#         left += 1
#         right -= 1

#     return arr


# arr = [8, 7, 1, 2, 3, 6, 5, 9]
# print(getHFDF(arr))

def solve():
    arr = [8, 7, 1, 2, 3, 9]
    arr.sort()
    n = len(arr)
    for i in range(n//2):
        print(arr[i], end=" ")
    for i in range(n-1, n//2-1, -1):
        print(arr[i], end=" ")


solve()
