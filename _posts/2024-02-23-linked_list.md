---
layout: post
title: Linked List
date: 2024-02-23
tags: dsa
toc: true
comments: true
---

# Concept

A [linked list](https://en.wikipedia.org/wiki/Linked_list) is a data structure that consists of a collection of nodes,
whose order is not related to their physical placement in memory.

Each node contains data and pointers which refer to different nodes in the sequence.
The first node in the list is called as `Head`, and the last node is called as `Tail`.
There are some variations in a linked list according to what each node points to sequentially.

## Singly Linked List

There is only one pointer in a node that refers to the next node in the sequence.

{% highlight terminal %}
    
    Head                                                          Tail
      |    +--------+    +--------+    +--------+    +--------+    |
      +--> | 21 | +-+--> | 42 | +-+--> | 19 | +-+--> | 37 | + | <--+
           +--------+    +--------+    +--------+    +--------+
    
{% endhighlight %}

The last node in a singly linked list has no pointer to the next node because it does not exist.

**It uses less memory but also its implementation is easy, whereas it does not provide access to previous nodes.**

## Doubly Linked List

There are two pointers that refers to the previous and next node, respectively.

{% highlight terminal %}
    
    Head                                                                          Tail
      |    +------------+    +------------+    +------------+    +------------+    |
      +--> |   | 21 | +-+--> |   | 42 | +-+--> |   | 19 | +-+--> |   | 37 | + | <--+
           | + |    |   | <--+-+ |    |   | <--+-+ |    |   | <--+-+ |    |   |
           +------------+    +------------+    +------------+    +------------+
    
{% endhighlight %}

Similarly, in a doubly linked list, the last node has no pointer to its next node,
and the first node has no pointer to its previous node.

**It takes twice as much memory as a singly linked list because of two pointers of each node,
but it can be traversed backwards.**

## Circular Linked List

Both ends of the linked list are connected.

In a singly linked list, the tail node refers to the head node.

{% highlight terminal %}
    
    Head                                                          Tail
      |    +--------+    +--------+    +--------+    +--------+    |
      +--> | 21 | +-+--> | 42 | +-+--> | 19 | +-+--> | 37 | + | <--+
           +--------+    +--------+    +--------+    +------|-+
             ^                                              |
             |                                              |
             +----------------------------------------------+
    
{% endhighlight %}

In a doubly linked list, the head and tail node refer to each other.

{% highlight terminal %}
    
             +--------------------------------------------------------------+
             |                                                              |
    Head     |                                                              v     Tail
      |    +-|----------+    +------------+    +------------+    +------------+    |
      +--> | | | 21 | +-+--> |   | 42 | +-+--> |   | 19 | +-+--> |   | 37 | + | <--+
           | + |    |   | <--+-+ |    |   | <--+-+ |    |   | <--+-+ |    | | |
           +------------+    +------------+    +------------+    +----------|-+
             ^                                                              |
             |                                                              |
             +--------------------------------------------------------------+
    
{% endhighlight %}

So, it can be traversed forwards and backwards from anywhere.

## When to use

1. Used to implement some other common abstract data types: List, Queue, Stack, and [Associative Arrays](https://en.wikipedia.org/wiki/Associative_array) (Often used in the implementation of adjacency lists for graphs)
2. Easy to create a circular list
3. Easy to model real world objects, such as trains, that are sequential
4. Used in separate chaining of certain Hash Table implementations to deal with hashing collisions

## Complexity

| Operation | Singly Linked | Doubly Linked |
|-|-|-|
| Search | $O(n)$ | $O(n)$ |
| Insert at head | $O(1)$ | $O(1)$ |
| Insert at tail | $O(1)$ | $O(1)$ |
| Insert at middle | $O(n)$ | $O(n)$ |
| Delete at head | $O(1)$ | $O(1)$ |
| Delete at tail | $O(n)$ | $O(1)$ |
| Delete at middle | $O(n)$ | $O(n)$ |

- $n$ is the number of nodes.
- Peeking(=getting an index) from a linked list takes linear time as it traverses from head to tail.
- Deleting a node in the middle of a linked list requires to find the previous node of the node to be deleted.
  - It is why deletion at the tail in a singly linked list takes linear time as it traverses from head to tail.
  - But, a doubly linked list does not have to do that as the tail node has the pointer to the previous node.

# Implementation

The two classes have a common interface but perform slightly different operations depending on the class.

## Singly Linked List

<details>
<summary>Python</summary>

{% highlight python linenos %}
''' Long Comment '''
# This is comment
def main(x: int) -> None:
    print("Hello World")
{% endhighlight %}

</details>

### Search

{% highlight python linenos %}
class SinglyLinkedList:
    # skip ...

    def search(self, data: int) -> Node:
        node = self.head
        while node != self.tail:
            if node.data == data:
                break
            node = node.next
        return node
{% endhighlight %}




### Insertion

{% highlight python linenos %}
class SinglyLinkedList:
    # skip ...

    def insert_at(self, data: int) -> Node:
        pass
{% endhighlight %}

TBD

### Deletion

{% highlight python linenos %}
''' Long Comment '''
# Iterative
def main(x: int) -> None:
    print("Hello World")

# Recursive
{% endhighlight %}

TBD

## Doubly Linked List

<details>
<summary>Source Code</summary>

{% highlight python linenos %}
''' Long Comment '''
# This is comment
def main(x: int) -> None:
    print("Hello World")
{% endhighlight %}

</details>

### Class

TBD

### Insertion

{% highlight python linenos %}
''' Long Comment '''
# Iterative
def main(x: int) -> None:
    print("Hello World")

# Recursive
{% endhighlight %}

TBD

### Deletion

{% highlight python linenos %}
''' Long Comment '''
# Iterative
def main(x: int) -> None:
    print("Hello World")

# Recursive
{% endhighlight %}

TBD

# Application

## Linked List vs. Dynamic Array

Time and Space Complexity

Why?

## Reverse

TBD

## ZigZag

TBD

## Leetcode

TBD
