descriptions = {
    "Bubble Sort": (
        "Bubble Sort is a simple comparison-based algorithm where adjacent elements "
        "are repeatedly swapped if they are in the wrong order. The largest elements 'bubble' "
        "to the end in each pass. Easy to implement but inefficient for large datasets."
    ),
    "Selection Sort": (
        "Selection Sort repeatedly selects the minimum element from the unsorted part "
        "and moves it to the beginning. It performs fewer swaps but more comparisons."
    ),
    "Insertion Sort": (
        "Insertion Sort builds the sorted array one item at a time by comparing each new "
        "element with those already sorted and inserting it at the right position."
    ),
    "Merge Sort": (
        "Merge Sort is a divide-and-conquer algorithm. It divides the array into halves, "
        "recursively sorts them, and merges the sorted halves. Efficient and stable."
    ),
    "Quick Sort": (
        "Quick Sort is a divide-and-conquer algorithm that picks a pivot and partitions the array "
        "such that elements less than pivot are on the left and greater are on the right. It then "
        "recursively sorts the partitions. Fast but not stable."
    ),
    "Heap Sort": (
        "Heap Sort converts the array into a max heap, repeatedly extracts the maximum element, "
        "and places it at the end. It's an efficient in-place sorting method using the heap property."
    ),
    "Counting Sort": (
        "Counting Sort counts the number of occurrences of each element, then calculates positions "
        "based on cumulative counts. Best suited for small-range integers."
    ),
    "Radix Sort": (
        "Radix Sort processes elements digit by digit, using Counting Sort internally for each digit. "
        "Works best on fixed-length integers. It's non-comparative and stable."
    ),
    "Shell Sort": (
        "Shell Sort is an optimization of Insertion Sort that allows exchanges of far-apart elements. "
        "It uses a gap sequence to gradually reduce the gap to 1, leading to a final Insertion Sort pass."
    ),
    "Comb Sort": (
        "Comb Sort improves on Bubble Sort by comparing elements at a fixed gap apart, "
        "which gradually shrinks over time. This helps eliminate small values (turtles) "
        "from the end of the list early. When the gap reduces to 1, it behaves like Bubble Sort."
    ),
    "Tree Sort": (
        "Tree Sort uses a Binary Search Tree to insert all the elements, then performs an "
        "in-order traversal to retrieve them in sorted order. It's efficient if the tree "
        "is balanced, but can degrade with skewed trees."
    ),
    "Bucket Sort": (
        "Bucket Sort distributes elements into a number of buckets. Each bucket is then "
        "sorted individually (commonly with Insertion Sort), and finally, all buckets are merged. "
        "It's particularly efficient for uniformly distributed input."
    ),
    "Tim Sort": (
        "Tim Sort is a hybrid sorting algorithm derived from Merge Sort and Insertion Sort. "
        "It's the default in Python and Java for good reason: it divides the list into small runs, "
        "sorts each run with Insertion Sort, and then merges them efficiently."
    )
}
