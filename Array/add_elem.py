def addElem(arr, inBegin, inEnd, inPos):
    new_arr = [inBegin] + arr[:inPos[1]-1] + \
        [inPos[0]] + arr[inPos[-1]-1:] + [inEnd]

    return new_arr


arr = [1, 2, 3, 4, 5]
inBegin = 6
inEnd = 7
inPos = [8, 4]

print(addElem(arr, inBegin, inEnd, inPos))
