Day 44 – Doubly Linked List
📅 Date

August 24, 2026

🎯 Goal

Practice handling duplicate nodes in a Doubly Linked List while maintaining correct prev and next connections.

📚 Topic Covered
Doubly Linked List
Removing Duplicates
Pointer Manipulation
Maintaining prev and next
✅ Problem Solved
Remove Duplicates from a Sorted Doubly Linked List

Platform: GeeksforGeeks

Goal: Keep only one occurrence of every value.

Example
Input:
1 ⇄ 1 ⇄ 2 ⇄ 3 ⇄ 3 ⇄ 4

Output:
1 ⇄ 2 ⇄ 3 ⇄ 4

Approach:

Traverse the DLL using curr.
If curr.data == curr.next.data, remove the duplicate node.
Update both next and prev pointers correctly.
Otherwise, move to the next node.

Time Complexity: O(n)
Space Complexity: O(1)

🧠 Key Learning

In a DLL, deleting a duplicate requires updating both directions:

curr.next = curr.next.next
curr.next.prev = curr

Always check whether curr.next is None before accessing it.

🚀 Progress
✅ Day 44 Completed
🔥 44/100 Days of DSA
📌 Doubly Linked List: Duplicate Removal
