def find_median(arr):
    arr.sort()
    n = len(arr)

    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2


arr_odd = [3, 1, 2]
arr_even = [4, 7, 1, 2, 5, 6]

print(find_median(arr_odd))
print(find_median(arr_even))
