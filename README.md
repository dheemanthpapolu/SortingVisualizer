# 🧮 Sorting Algorithm Visualizer

A clean, animated and interactive **Python GUI tool** to visualize classic sorting algorithms step-by-step.  
Built using **Tkinter**, with modular code design for easy extension and customization.

---

## ✨ Features

- Real-time visual sorting animations
- Adjustable array size and speed control
- Algorithm selection dropdown
- Pause / Resume controls
- Step-by-step mode with **Next Step** control
- Dark / Light mode toggle
- Algorithm descriptions
- Time and space complexity viewer
- Fully modular file structure

---

## 📁 Folder Structure

```
SortingVisualizer/
├── main.py                    # GUI launcher
├── core/
│   ├── controls.py           # All control UI logic
│   ├── draw.py               # Canvas drawing logic
│   ├── sorter.py             # Maps algorithms to names
│   ├── descriptions.py       # Algorithm descriptions
│   └── complexity_info.py    # Time & space complexities
├── algorithms/
│   ├── bubble_sort.py
│   ├── insertion_sort.py
│   ├── selection_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   ├── heap_sort.py
│   ├── counting_sort.py
│   ├── radix_sort.py
│   ├── shell_sort.py
│   ├── comb_sort.py
│   ├── tree_sort.py
│   ├── bucket_sort.py
│   └── tim_sort.py
```

---

## 🔢 Algorithms Included

- Bubble Sort
- Insertion Sort
- Selection Sort
- Merge Sort
- Quick Sort
- Heap Sort
- Counting Sort
- Radix Sort
- Shell Sort
- Comb Sort
- Tree Sort
- Bucket Sort
- Tim Sort

---

## 🚀 How to Run

Make sure Python is installed.  
Then from terminal:

```bash
cd path/to/SortingVisualizer
python main.py
```

This will launch the GUI.

---

## ➕ How to Add New Sorting Algorithms

1. Create a new file in the `algorithms/` folder like `your_sort.py`
2. Inside it, implement a generator function:
```python
def your_sort(arr):
    # yield arr, highlights
```
3. Import and register it in `core/sorter.py`:
```python
from algorithms.your_sort import your_sort
algorithm_map["Your Sort"] = your_sort
```

Done — it appears in the dropdown.

---

## 📌 Roadmap / Ideas

- [x] Modular sort files
- [x] Canvas animation
- [x] Pause & Resume
- [x] Step-by-step mode
- [x] Dark/Light mode toggle
- [x] Algorithm descriptions
- [x] Time & space complexity viewer

---

## 📄 License

[MIT](https://opensource.org/licenses/MIT)

---

