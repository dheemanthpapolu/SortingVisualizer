def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for i, num in enumerate(arr):
        count[num] += 1
        yield arr, [i]

    index = 0
    for i, c in enumerate(count):
        while c > 0:
            arr[index] = i
            yield arr, [index]
            index += 1
            c -= 1
