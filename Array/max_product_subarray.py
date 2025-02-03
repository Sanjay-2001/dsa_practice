def maxProduct(arr, n):
    # Initialize the max and min products at the first element
    max_prod = min_prod = result = arr[0]

    # Traverse through the array
    for i in range(1, n):
        # If the current element is negative, we swap max_prod and min_prod
        if arr[i] < 0:
            max_prod, min_prod = min_prod, max_prod

        # Calculate max and min product so far
        max_prod = max(arr[i], max_prod * arr[i])
        min_prod = min(arr[i], min_prod * arr[i])

        # Update the result with the maximum product found so far
        result = max(result, max_prod)

    print("Maximum Product: ", result)


arr = [1, 2, -3, 0, -4, -5]
N = len(arr)
maxProduct(arr, N)
