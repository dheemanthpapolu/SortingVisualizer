def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        up = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > up:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = up
    return bucket

def bucket_sort(arr):
    if len(arr) == 0:
        return
    max_val = max(arr)
    size = max_val / len(arr)

    buckets = [[] for _ in range(len(arr))]

    for i in range(len(arr)):
        index = int(arr[i] / size)
        if index != len(arr):
            buckets[index].append(arr[i])
        else:
            buckets[len(arr) - 1].append(arr[i])
        yield arr, [i]

    k = 0
    for bucket in buckets:
        insertion_sort(bucket)
        for val in bucket:
            arr[k] = val
            yield arr, [k]
            k += 1
