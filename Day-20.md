# Day 20 – Arrays (Advanced Algorithms)

## 📅 Date

July 24, 2026

## 🎯 Goal

Master advanced array algorithms involving merge sort, mathematical observations, and dynamic programming patterns commonly asked in FAANG and product-based company interviews.

---

## 📚 Topics Covered

* Merge Sort
* Divide & Conquer
* Mathematical Approach
* Dynamic Programming
* Array Optimization

---

## ✅ Problems Solved

### 1. Merge Two Sorted Arrays Without Extra Space

**Platform:** GeeksforGeeks

**Approach:**

* Applied the **Gap Method (Shell Sort Technique)**.
* Compared elements at a shrinking gap until the arrays became fully sorted.

**Time Complexity:** O((n + m) log(n + m))

**Space Complexity:** O(1)

---

### 2. Find the Repeating and Missing Number

**Platform:** GeeksforGeeks

**Approach:**

* Used mathematical equations (sum and sum of squares) to determine the repeating and missing numbers efficiently.

**Time Complexity:** O(n)

**Space Complexity:** O(1)

---

### 3. Count Inversions

**Platform:** GeeksforGeeks

**Approach:**

* Modified Merge Sort to count inversions while merging two sorted halves.

**Time Complexity:** O(n log n)

**Space Complexity:** O(n)

---

### 4. Reverse Pairs

**Platform:** LeetCode (LC 493)

**Approach:**

* Extended the Merge Sort algorithm.
* Counted valid reverse pairs before merging each half.

**Time Complexity:** O(n log n)

**Space Complexity:** O(n)

---

### 5. Maximum Product Subarray

**Platform:** LeetCode (LC 152)

**Approach:**

* Maintained both the maximum and minimum product ending at each index because a negative number can swap their roles.

**Time Complexity:** O(n)

**Space Complexity:** O(1)

---

## 🧠 Key Learnings

* Merge Sort is useful beyond sorting—it solves inversion and reverse pair problems efficiently.
* Mathematical formulas can eliminate the need for extra data structures.
* Tracking both maximum and minimum values is essential for product-based subarray problems.
* Choosing the correct algorithm reduces brute-force solutions from **O(n²)** to **O(n log n)** or **O(n)**.

---

## 🚀 Progress

* ✅ Day 20 Completed
* 🔥 Current Streak: 20/100

---

## 📌 Next Goal

Start Linked Lists by learning reversal, cycle detection, middle node, and merge operations.
