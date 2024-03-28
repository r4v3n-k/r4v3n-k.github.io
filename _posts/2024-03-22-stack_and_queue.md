---
layout: post
title: Stack vs. Queue
date: 2024-03-22
tags: dsa
toc: true
comments: true
---

# Concept

## Stack

A [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) is a data structure that serves as a collection of elements.
Each is added or removed in the way known as **the last in, first out (LIFO)**, where the most recently added element should be removed first.

<div class="img_row">
    <img class="col" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Lifo_stack.svg/350px-Lifo_stack.svg.png">
</div>

As shown above, it is a one-ended linear data structure with providing three main operations:
- `push()`, `pop`, and `peek()`
- Peeking is to read the element at the top of a stack.

### When to use

1. Used by undo mechanisms in text editors.
2. Used in compiler syntax checking for matching barckets and braces.
	- E.g., Given a string made up of the following brackets: `()[]{}`, determine whether the brackets properly match.
		- `[{}]` -> valid
		- `(()())` -> valid
		- `{]` -> invalid
	- Solution: Push open brackets into a stack. And whenever we find a closed (or reversed) bracket in a bracket sequence, compare the top of a stack to the opposite of the current bracket. If it matches, pop it. Finally, an empty stack means all brackets matched.
3. Used for modeling a pile of books or plates.
    - E.g., Tower of Hanoi -> Move piles to the most right so that smaller piles are up in order.
4. Used behind the scenes to support recursion by keeping track of previous function calls.
5. Used in a Depth First Search (DFS) graph traversal.

### Interface

{% plantuml %}
skinparam ClassAttributeIconSize 0
class Stack {
    -_linear_ds  :list[object]
    -_top :int
    +size() :int
    +is_empty() :bool
    +peek() :object
    +push(object) :None
    +pop() :object
    +contain(object) :bool
    +remove(object) :bool
}
{% endplantuml %}

### Complexity

| Operation | Time |
|-|-|
| Size | $O(1)$ |
| Peek | $O(1)$ |
| Push | $O(1)$ |
| Pop | $O(1)$ |
| Contain | $O(n)$ |
| Remove | $O(n)$ |

- To remove a certain element, scanning through a stack is required.

## Queue

A [queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) is also a linear data structure
that serves as a collection of elements in the way, **the first in, first out (FIFO)**,
where the latest added element should be removed first.

<div class="img_row">
    <img class="col" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/220px-Data_Queue.svg.png">
</div>

As shown above, it provides four primary operations:
- `enqueue()`, `dequeue()`, `peek_front()` and `peek_back()`
- The latest queued element positions at the front of a queue.
- The most recent queued element positions at the back of a queue.

### When to use

1. Any waiting line models a queue. E.g., a lineup at a move theatre or a restaurant.
2. Used for tracking the X most recently added elements.
3. Web server request management where you want first come first serve.
4. Used in a Breadth First Search (BFS) graph traversal.

### Interface

{% plantuml %}
skinparam ClassAttributeIconSize 0
class Queue {
    -_linear_ds  :list[object]
    -_front :int
    -_back :int
    +size() :int
    +is_empty() :bool
    +enqueue(object) :None
    +dequeue() :object
    +peek_front() :object
    +peek_back() :object
    +contain(object) :bool
    +remove(object) :bool
}
{% endplantuml %}

### Complexity

| Operation | Time |
|-|-|
| Size | $O(1)$ |
| Enqueue | $O(1)$ |
| Dequeue | $O(1)$ |
| Peek | $O(1)$ |
| Contain | $O(n)$ |
| Remove | $O(n)$ |

- To remove a certain element, scanning through a queue is required.

# Implementation

## Stack

- [Source Code](https://github.com/robin-kkk/practical-python/tree/main/dsa/stack)

## Queue

- [Source Code](https://github.com/robin-kkk/practical-python/tree/main/dsa/queue)

## Deque

In Python, there is a very useful linear data structure, `deque` which is a bi-directional queue.
- It allows us to add or remove an element both back and forth.

{% highlight python linenos %}
from collections import deque
dq =  deque([1, 2, 3])
dq.append(4) # [1, 2, 3, 4]
dq.appendleft(0) # [0, 1, 2, 3, 4]
assert dq.pop() == 4
assert dq.popleft() == 0
print(dq) # deque([1, 2, 3])

dq.extend([1, 2, 2])
print(dq) # deque([1, 2, 3, 1, 2, 2])
dq.extendleft([4, 5, 6])
print(dq) # deque([6, 5, 4, 1, 2, 3, 1, 2, 2])
assert dq.index(1) == 3
assert dq.count(2) == 3

dq.remove(1)
print(dq) # deque([6, 5, 4, 2, 3, 1, 2, 2])
dq.reverse()
print(dq) # deque([2, 2, 1, 3, 2, 4, 5, 6])
dq.insert(3, 99)
assert dq[3] == 99
print(dq) # deque([2, 2, 1, 99, 3, 2, 4, 5, 6])

dq.rotate(1)
print(dq) # deque([6, 2, 2, 1, 99, 3, 2, 4, 5])
dq.rotate(4)
print(dq) # deque([3, 2, 4, 5, 6, 2, 2, 1, 99])

dq.clear()
{% endhighlight %}

# Application

## Monotonic Stack

A [monotonic stack](https://www.geeksforgeeks.org/introduction-to-monotonic-stack-data-structure-and-algorithm-tutorials/)
contains elements in monotonically either increasing or decreasing order.

For an increasing order, it should not have a smaller element at top of each element.
- Iterate a given list of elements one by one. In each iteration,
  **keep popping greater elements out of a stack until it is empty or its top is smaller than the current element**.
  Then, push the current element into the stack.

Note that an increasing monotonic stack is used to find the nearest smaller element for each element.
 
{% highlight python linenos %}
"""
arr = [3, 2, 4, 1, 5, 7]

For i=0, stk = [3]
For i=1, stk = [2] (3 > 2)
For i=2, stk = [2, 4]
For i=3, stk = [1] (4 > 1 and 2 > 1)
For i=4, stk = [1, 5]
For i=5, stk = [1, 5, 7]

input: [3, 2, 4, 1, 5, 7]
output: [1, 5, 7]
               ^
              top
"""
def get_monotonic_increasing_stack(arr: list) -> list:
    stk = []
    for x in arr:
        while stk and stk[-1] > x:
            # Here, the current element is the next smaller element than the top of a stack.
            stk.pop()
        # Here, the top of a stack is the previous smaller element. 
        stk.append(x)
    return stk
{% endhighlight %}

For a decreasing order, it should not have a greater element at top of each element.
- Iterate a given list of elements one by one. In each iteration,
  **keep popping smaller elements out of a stack until it is empty or its top is greater than the current element**.
  Then, push the current element into the stack.

Note that a decreasing monotonic stack is used to find the nearest greater element for each element.

{% highlight python linenos %}
"""
arr = [3, 2, 4, 7, 5, 1]

For i=0, stk = [3]
For i=1, stk = [3, 2]
For i=2, stk = [4] (2 < 4 and 3 < 4)
For i=3, stk = [7] (4 < 7)
For i=4, stk = [7, 5]
For i=5, stk = [7, 5, 1]

input: [3, 2, 4, 7, 5, 1]
output: [7, 5, 1]
               ^
              top
"""
def get_monotonic_decreasing_stack(arr: list) -> list:
    stk = []
    for x in arr:
        while stk and stk[-1] < x:
            # Here, the current element is the next greater element than the top of a stack.
            stk.pop()
        # Here, the top of a stack is the previous greater element. 
        stk.append(x)
    return stk
{% endhighlight %}

Notice that the popped elements are not reused.

In summary, the monotonic stack problem is primarily to find **the nearest smaller or greater element** in an array.
Also, it can be to find the maximum and minimum elements in a certain range and keeps the order of elements in the range.
For that, we don't need to compare elements one by one again to get those elements if using a stack.

While it takes constant time to read the top of a stack, in memory space, it takes linear time in the worst case.

## Monotonic Queue/Deque

TBD

## Leetcode

- [Monotonic Stack](https://leetcode.com/tag/monotonic-stack/)
- [Monotonic Queue](https://leetcode.com/tag/monotonic-queue/)
- See my list related to [Stack]() and [Queue]()

