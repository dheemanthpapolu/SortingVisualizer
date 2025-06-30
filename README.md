# README.md content + template layout

# Sorting Algorithm Visualizer

A modular, Tkinter-based animated visualization tool for classic sorting algorithms. Built with clean file structure and extendability in mind.

---

## 📊 Features

- Visualize sorting steps in real time
- Adjustable array size and speed control
- Dropdown to choose algorithm
- Clean modular structure for easy addition of algorithms
- Color-coded animation for comparisons and swaps

---

## 📦 Project Structure

```plaintext
SortingVisualizer/
├── main.py                    # GUI controller
├── core/
│   ├── draw.py              # Handles all drawing to canvas
│   └── sorter.py            # Central algorithm mapping
├── algorithms/
│   ├── bubble_sort.py
│   ├── insertion_sort.py
│   ├── selection_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   └── heap_sort.py
```

---

## ⚡ How to Run

```bash
# Clone repo and run:
python main.py
```

---

## 🔢 Algorithms Included

- Bubble Sort
- Insertion Sort
- Selection Sort
- Merge Sort
- Quick Sort
- Heap Sort

---

## 🚀 Getting Started

To add a new algorithm:
1. Create `algorithms/your_sort.py`
2. Implement a generator `def your_sort(arr):`
3. Register it in `core/sorter.py`:
```python
from algorithms.your_sort import your_sort
algorithm_map["Your Sort"] = your_sort
```

That's it!

---

## 🌈 Roadmap

- [x] Modular sort files
- [x] Canvas animation
- [x] Dropdown menu UI
- [ ] Pause/Resume
- [ ] Step-by-step mode
- [ ] Side-by-side comparison
- [ ] Sound effects
- [ ] Export frames as GIF

---

## 💪 Contributing

Pull requests welcome. Please keep code modular and clean.

---

## 🚀 License

MIT
