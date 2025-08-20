# Python Programming Challenge

This repository contains solutions to the **Modest Tree 2022 Python programming test**.  
It demonstrates practical algorithm design, reasoning, and implementation choices,  
with a focus on correctness, clarity, and efficiency.

---

## Project Structure
```
programming_python/
│── __main__.py        # Entry point to run all questions
│── data
│── docs
│── Dockerfile
│── README.md
```

You can either:
- Run directly with **Python**:
  ```bash
  python -m programming_python
  ```
- Or build and run with **Docker**:
  ```bash
  docker build -t python-challenge .
  docker run --rm -it python-challenge
  ```

---

## Problem Breakdown

### Question 1 – [Problem Title]
- **Algorithm Used**: [e.g., Sorting + Binary Search]
- **Why**: Chosen for simplicity and logarithmic search speed.
- **Time Complexity**: O(n log n) (due to sort), O(log n) for lookups.
- **Space Complexity**: O(1) extra (in-place operations).
- **Expected Input/Output**:
  ```
  Input: [sample input]
  Output: [expected result]
  ```

---

### Question 2 – [Problem Title]
- **Algorithm Used**: [e.g., Hash Map lookups]
- **Why**: Provides O(1) average-time checks compared to O(n) linear scans.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n) for the hash table.
- **Expected Input/Output**:
  ```
  Input: [sample input]
  Output: [expected result]
  ```

---

### Question 3 – [Problem Title]
- **Algorithm Used**: [e.g., Two-pointer technique]
- **Why**: Optimizes space usage, avoids nested loops.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).
- **Expected Input/Output**:
  ```
  Input: [sample input]
  Output: [expected result]
  ```

---

### Question 4 – [Problem Title]
- **Algorithm Used**: [e.g., Dynamic Programming]
- **Why**: Avoids recomputation by caching subproblems.
- **Time Complexity**: O(n·m).
- **Space Complexity**: O(n·m).
- **Expected Input/Output**:
  ```
  Input: [sample input]
  Output: [expected result]
  ```

---

### Question 5 – [Problem Title]
- **Algorithm Used**: [e.g., Greedy approach]
- **Why**: Locally optimal choices lead to globally optimal results.
- **Time Complexity**: O(n log n).
- **Space Complexity**: O(1).
- **Expected Input/Output**:
  ```
  Input: [sample input]
  Output: [expected result]
  ```

---

## Full Expected Results

When running the full program:

```
$ python -m programming_python
Question 1 → Result: [value]
Question 2 → Result: [value]
Question 3 → Result: [value]
Question 4 → Result: [value]
Question 5 → Result: [value]

All questions executed successfully!
```

---

## Design Philosophy

- Prefer **Python built-ins** where they offer efficient, clear solutions.
- Explicit over implicit: every step is clear to the reader/interviewer.
- Balanced trade-offs: correctness and maintainability are prioritized, while also noting potential optimizations.
- Code formatted using **Black** for consistency.

---

## Challenges & Solutions

1. **Challenge**: Efficient lookup and search.  
   **Solution**: Used hash maps and binary search where appropriate.

2. **Challenge**: Avoiding unnecessary recomputation.  
   **Solution**: Applied memoization / dynamic programming.

3. **Challenge**: Keeping code clean for interview readability.  
   **Solution**: Modularized by question, added comments, and kept functions concise.

---

## Conclusion

This project demonstrates:
- Knowledge of multiple algorithmic strategies.  
- Awareness of time/space complexity trade-offs.  
- Ability to communicate not just *what* the code does, but *why*.  

This README serves as both **technical documentation** and a guide to the interviewer.
