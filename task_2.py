def binary_search_upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        middle = (left + right) // 2
        middle_value = arr[middle]

        if middle_value >= target:
            upper_bound = middle_value
            right = middle - 1
        else:
            left = middle + 1

    return iterations, upper_bound


if __name__ == "__main__":
    data = [1.1, 2.5, 3.0, 4.4, 5.9]
    print(binary_search_upper_bound(data, 3.0))
    print(binary_search_upper_bound(data, 3.7))
    print(binary_search_upper_bound(data, 6.0))
