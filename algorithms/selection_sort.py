def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            yield arr, [min_idx, j]
            if arr[j] < arr[min_idx]:
                min_idx = j
                yield arr, [min_idx]
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr, [i, min_idx]
    yield arr, []
