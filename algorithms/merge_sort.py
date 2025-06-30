def merge_sort(arr):
    def merge_sort_helper(arr, l, r):
        if l < r:
            m = (l + r) // 2
            yield from merge_sort_helper(arr, l, m)
            yield from merge_sort_helper(arr, m + 1, r)
            yield from merge(arr, l, m, r)

    def merge(arr, l, m, r):
        left = arr[l:m + 1]
        right = arr[m + 1:r + 1]
        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            yield arr, [k]
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            yield arr, [k]
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            yield arr, [k]
            arr[k] = right[j]
            j += 1
            k += 1

    yield from merge_sort_helper(arr, 0, len(arr) - 1)
    yield arr, []
