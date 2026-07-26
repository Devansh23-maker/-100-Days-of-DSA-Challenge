# Day 21 – Arrays (Sliding Window & Optimization)

## 📅 Date

July 25, 2026

## 🎯 Goal

Strengthen advanced array problem-solving using two pointers, greedy algorithms, prefix/suffix optimization, and dynamic programming.

---

## 📚 Topics Covered

* Two Pointers
* Greedy
* Prefix & Suffix Arrays
* Kadane's Algorithm
* Optimization Techniques

---

## ✅ Problems Solved

### 1. Trapping Rain Water

**Platform:** LeetCode (LC 42)

**Approach:**

* Used the Two Pointer technique.
* Maintained leftMax and rightMax while moving pointers inward to calculate trapped water.

**Time Complexity:** O(n)

**Space Complexity:** O(1)

---

### 2. Stock Buy and Sell – Max One Transaction Allowed

**Platform:** GeeksforGeeks

**Approach:**

* Kept track of the minimum buying price seen so far.
* Updated the maximum profit at each step.

**Time Complexity:** O(n)

**Space Complexity:** O(1)

---

### 3. Maximum Subarray Sum by Removing At Most One Element

**Platform:** GeeksforGeeks

**Approach:**

* Computed maximum subarray sums from both left and right.
* Combined prefix and suffix results to evaluate the best answer after removing one element.

**Time Complexity:** O(n)

**Space Complexity:** O(n)

---

### 4. Container With Most Water

**Platform:** LeetCode (LC 11)

**Approach:**

* Applied the Two Pointer technique.
* Moved the pointer with the smaller height to maximize the container area.

**Time Complexity:** O(n)

**Space Complexity:** O(1)

---

## 🧠 Key Learnings

* Two Pointers can reduce brute-force solutions from **O(n²)** to **O(n)**.
* Greedy algorithms work well when maintaining the best value seen so far.
* Prefix and suffix computations are useful for deletion and optimization problems.
* Many interview problems revolve around maximizing or minimizing a value in a single traversal.

---

## 🚀 Progress

* ✅ Day 21 Completed
* 🔥 Current Streak: 21/100

---

## 📌 Next Goal

Begin **Linked Lists** by learning reversal, middle node, cycle detection, and merge operations.
