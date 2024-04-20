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
contains elements in monotonic order, either increasing or decreasing.

In an increasing order, it should have the greatest element at the top in every iteration.

- While iterating an array, in each iteration,
  **keep popping greater elements out of the stack until it is empty or its top is smaller than the current element**.
  Then, push the current element into the stack.

Note that the increasing monotonic stack is used to **find the nearest smaller element for each element**.
 
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

In a decreasing order, it should have the smallest element at the top in every iteration.

- While iterating an array, in each iteration,
  **keep popping smaller elements out of the stack until it is empty or its top is greater than the current element**.
  Then, push the current element into the stack.

Note that the decreasing monotonic stack is used to **find the nearest greater element for each element**.

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

In summary, the monotonic stack problem primarily aims to **find the nearest smaller or greater element** in an array.
Also, it can be used to find the maximum or minimum element in a certain range while keeping the order of elements in the range.
For that, we do not need to compare elements one by one again to find the element we want if using a stack.
- It takes constant time! But, it takes linear space complexity in the worst case.

## Monotonic Queue

A [monotonic queue](https://www.geeksforgeeks.org/introduction-to-monotonic-queues/) contains elements in monotonically either increasing or decreasing order.

The monotonic queue is usually implemented by a deque (double-ended queue) container
that allows efficient insertion and deletion of elements from both the front and back of the queue.

In an increasing order, the last element (at the back of the deque) greater than the current element is removed.

- While iterating an array, in each iteration,
  **keep popping greater elements out of the back until it is empty or the last element is smaller than the current element**.
  Then, enqueue the current element which positions at the front of the queue.

Keep in mind that the increasing monotonic queue is used to **find the minimum element in a sliding window technique**
because the first element in the queue is the minimum value among elements we have seen.

{% highlight python linenos %}
"""
arr = [3, 2, 4, 1, 5, 7]

For i=0, dq = [3]
For i=1, dq = [2] (3 > 2)
For i=2, dq = [2, 4]
For i=3, dq = [1] (4 > 1 and 2 > 1)
For i=4, dq = [1, 5]
For i=5, dq = [1, 5, 7]

input: [3, 2, 4, 1, 5, 7]
output: [1, 5, 7]
         ^     ^
      front   back
"""
def get_monotonic_increasing_deque(arr: list) -> list:
    n = len(arr)
    dq = deque()
    for i in range(n):
        while dq and arr[dq[-1]] > arr[i]:
            dq.pop()
        dq.append(i)
        print(f'The minimum value when going through arr[0:{i}]: {arr[dq[0]]}')
    return list(dq)
{% endhighlight %}

Furthermore, to find all the minimum values in a fixed-size window,
we can consider the difference between the first element in the deque and the current index.

While iterating an array, in each iteration,
- If the difference is less than the window size, dequeue the first element out of the deque.
- Then, pop greater elements out of the back of the deque, and push the current element.
- From the current index greater than the window size, the first element in the deque is always the minimum value.

{% highlight python linenos %}
def find_minimum_value_of_window(arr: list, window_size: int) -> list:
    n = len(arr)
    dq = deque()
    ans = []
    for i in range(n):
        # Expand the window to the right.
        while dq and arr[dq[-1]] > arr[i]:
            dq.pop()
        dq.append(i)
        # Shrink the window from the left.
        while dq and dq[0] <= i - window_size:
            dq.popleft()
        # Find the minimum.
        if i >= window_size - 1:
            ans.append(arr[dq[0]])
    return ans
{% endhighlight %}

Also, it can be helpful to solve a dynamic programming problem such as LIS (longest increasing subsequence).

For instance, when choosing the minimum value among candidates of K subproblems,
we can use a monotonic deque on `DP[]` array instead of `arr[]`.
- [LeetCode 2944. Minimum Number of Coins for Fruits](https://leetcode.com/problems/minimum-number-of-coins-for-fruits)

{% highlight python linenos %}
"""
NOTE: Zero-indexed
- Be able to skip the next (i+1) elements when taking the i-th element

dp[i] = arr[i] + min(dp[i+1:2*(i+1)])
"""
# O(n^2)
def find_minimum_value_of_dp(arr: list) -> int:
    n = len(prices)
    dp = [int(1e9)]*(n+1)
    dp[n] = 0
    for i in range(n-1, -1, -1):
        j = min(n, 2*(i+1))
        dp[i] = prices[i] + min(dp[i+1:j+1])

# O(n)
def find_minimum_value_of_dp_optimized(arr: list) -> int:
    n = len(prices)
    dp = [0]*(n+1)
    inc_dq = deque([n])
    # Slide window from right to left.
    for i in range(n-1, -1, -1):
        # Shrink the window.
        j = min(n, 2*(i+1))
        while inc_dq[0] > j:
            inc_dq.popleft()
        # dp[inc_dq[0]] := the minimum value in the current window. 
        dp[i] = arr[i] + dp[inc_dq[0]]
        # Expand the window.
        while inc_dq and dp[inc_dq[-1]] > dp[i]:
            inc_dq.pop()
        inc_dq.append(i)
    return dp[0]
{% endhighlight %}

Another instance is that the window has a constraint (not a fixed-length):
- The sum of elemetns in the window should equal to a given integer.
- The sum of elements in the window should be less/greater than a given integer.

With that, most problems asks us how to find:
- the maximum or minimum length of the window that satisfies the constraint.
- a specific window that satisfies the constraint (Here is only one single window)

Finally, it needs to pay attention to when shrinking the window from the left.
- Need to check whether the current window satisfies a given constraint.
- If it is, that window is one of candidates to our solution.
- [LeetCode 862. Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k)

{% highlight python linenos %}
def find_minimum_window_with_sum_at_least_k(arr: list[int], k: int) -> list:
    n = len(arr)

    # Build a prefix sum array.
    psum = [0]*(n+1)
    for i in range(n):
        psum[i+1] = psum[i] + arr[i]
    
    ans = int(1e9)
    dq = deque()
    for i in range(n+1):
        # Expand the window to the right.
        while dq and psum[dq[-1]] > psum[i]:
            dq.pop()
        dq.append(i)
        # Shrink the window from the left.
        while dq and psum[dq[-1]] - psum[dq[0]] >= k:
            # Find the minimum window.
            ans = min(ans, dq[-1] - dq[0])
            dq.popleft()
    return ans if ans != int(1e9) else -1
{% endhighlight %}

In a decreasing order, the last element (at the back of the deque) smaller than the current element is removed.

- While iterating an array, in each iteration,
  **keep popping smaller elements out of the back until it is empty or the last element is greater than the current element**.
  Then, enqueue the current element which positions at the front of the queue.

Note that the decreasing monotonic queue is used to **find the maximum element in a sliding window**.
- The first element in the decreasing deque is the maximum value among elements we have seen.

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
         ^     ^
      front   back
"""
def get_monotonic_decreasing_deque(arr: list) -> list:
    n = len(arr)
    dq = deque()
    for i in range(n):
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)
        print(f'The maximum value when going through arr[0:{i}]: {arr[dq[0]]}')
    return list(dq)
{% endhighlight %}

Similarly to the increasing queue, to find all the maximum values in a fixed-size window,
we can consider the difference between the first element in the deque and the current index.

{% highlight python linenos %}
def find_maximum_value_of_window(arr: list, window_size: int) -> list:
    n = len(arr)
    dq = deque()
    ans = []
    for i in range(n):
        # Expand the window to the right.
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)
        # Shrink the window from the left.
        while dq and dq[0] <= i - window_size:
            dq.popleft()
        # Find the maximum.
        if i >= window_size - 1:
            ans.append(arr[dq[0]])
    return ans
{% endhighlight %}

Also, it can be helpful to solve a dynamic programming problem such as LDS (longest decreasing subsequence).

Similary to using an increasing deque, when choosing the maximum value among candidates of K subproblems,
we can use a monotonic deque on `DP[]` array instead of `arr[]`

Sometimes, we encounter problems to be solved with both types of deque such as:
1. The absolute difference between any two elements in the window should be less/greater or equal to than a given integer.
2. The maximum absolute difference can be calculated by (the maximum value - the minimum value) in the window.
   - [LeetCode 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit)

See the types using a sliding window techinque.
- [GeeksForGeeks: Window Sliding Technique](https://www.geeksforgeeks.org/window-sliding-technique/)

## Leetcode

- [Monotonic Stack](https://leetcode.com/tag/monotonic-stack/)
- [Monotonic Queue](https://leetcode.com/tag/monotonic-queue/)
- See my list related to [Stack](https://leetcode.com/list/pfafbwgj) and [Queue](https://leetcode.com/list/mhacd9rd)

