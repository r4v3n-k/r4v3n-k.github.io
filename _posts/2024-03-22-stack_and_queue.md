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

A [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) is a data structure that serves as
a collection of elements, each of which is added or removed by the last in, first out (`LIFO`).

![LIFO.png](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Lifo_stack.svg/350px-Lifo_stack.svg.png)

As shown above, it is a one-ended linear data structure with providing three main operations:
- `push()`, `pop`, and `peek()`
- Peeking is to read the element at the top of a stack.

### When to use

TBD

### Complexity

| Operation | Time |
|-|-|
| Push | $O(1)$ |
| Pop | $O(1)$ |
| Peek | $O(1)$ |
| Search | $O(n)$ |
| Size | $O(1)$ |
| Removal | $O(n)$ |

- To remove a certain element, scanning through a stack is required.

## Queue

A [queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) is also a linear data structure
where an elements is added or removed by the first in, first out (`FIFO`).

![FIFO.png](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/220px-Data_Queue.svg.png)

As shown above, it provides four main operations:
- `enqueue()`, `dequeue()`, `front()` and `back()`
- The latest queued element positions at the most front of a queue.
- The most recent queued element positions at the most back of a queue.

### When to use

TBD

### Complexity

| Operation | Time |
|-|-|
| Enqueue | $O(1)$ |
| Dequeue | $O(1)$ |
| Front | $O(1)$ |
| Back | $O(1)$ |
| Search | $O(n)$ |
| Size | $O(1)$ |
| Removal | $O(n)$ |

- To remove a certain element, scanning through a queue is required.

# Implementation

## Stack Interface

plantuml

{% highlight python linenos %}
''' Long Comment '''
# This is comment
def main(x: int) -> None:
    print("Hello World")
{% endhighlight %}

TBD

## Queue Interface

plantuml

TBD

# Application

## What is monotonic stack and queue

## Leetcode

- [Monotonic Stack](https://leetcode.com/tag/monotonic-stack/)
- [Monotonic Queue](https://leetcode.com/tag/monotonic-queue/)
- See my list related to [Stack]() and [Queue]()

