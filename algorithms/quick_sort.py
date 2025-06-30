def quick_sort(arr):
    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = yield from partition(arr, low, high)
            yield from quick_sort_helper(arr, low, pi - 1)
            yield from quick_sort_helper(arr, pi + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            yield arr, [j, high]
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                yield arr, [i, j]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        yield arr, [i + 1, high]
        return i + 1

    yield from quick_sort_helper(arr, 0, len(arr) - 1)
    yield arr, []
