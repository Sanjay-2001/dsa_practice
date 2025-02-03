def removeDuplicates(arr):
    # new_arr = []
    # for num in arr:
    #     if num not in new_arr:
    #         new_arr.append(num)

    # print(new_arr)

    return list(dict.fromkeys(arr))


arr = [2, 3, 1, 9, 3, 1, 3, 9]
print(removeDuplicates(arr))
