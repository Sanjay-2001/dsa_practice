def getSumOfElements(arr):
    sum = 0
    for num in arr:
        sum += num

    return sum
    # return (len(arr) * (len(arr)+1))//2  # for n natural numbers


arr = [1, 2, 3, 4, 5, 5]
print(getSumOfElements(arr))
