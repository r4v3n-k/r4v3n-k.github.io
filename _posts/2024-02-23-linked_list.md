---
layout: post
title: Linked List
date: 2024-02-23
tags: dsa
toc: true
comments: true
---

# Concept

A [linked list](https://en.wikipedia.org/wiki/Linked_list) is a data structure that consists of a collection of nodes
whose order is not related to their physical placement in memory.

Each node contains data and pointers which refer to different nodes in the sequence.
The first node in the list is called `Head`, and the last is called `Tail`.
There are many different variations for a linked list according to what each node points to sequentially.

## Singly Linked List

There is only one pointer in a node that refers to the next node in the sequence.

The tail node in a singly linked list has no pointer to the next node because the next node does not exist.
In addition, the singly linked list does not provide access to previous nodes from every node.

{% highlight terminal %}
    
    Head                                                          Tail
      |    +--------+    +--------+    +--------+    +--------+    |
      +--> | 21 | +-+--> | 42 | +-+--> | 19 | +-+--> | 37 | + | <--+
           +--------+    +--------+    +--------+    +--------+
    
{% endhighlight %}

But, **its implementation is straightforward and uses less memory.**

## Doubly Linked List

A node has two pointers which refer to the previous and next nodes, respectively.

In a doubly linked list, the tail node has no next node, and the head has no previous node.

{% highlight terminal %}
    
    Head                                                                          Tail
      |    +------------+    +------------+    +------------+    +------------+    |
      +--> |   | 21 | +-+--> |   | 42 | +-+--> |   | 19 | +-+--> |   | 37 | + | <--+
           | + |    |   | <--+-+ |    |   | <--+-+ |    |   | <--+-+ |    |   |
           +------------+    +------------+    +------------+    +------------+
    
{% endhighlight %}

**It takes twice as much memory as a singly linked list because of two pointers of each node,
but it can be traversed backward.**

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

In a doubly linked list, the head and tail nodes refer to each other.

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

So, it can be traversed forward and backward from anywhere.

## When to use

1. Used to implement some other common abstract data types: List, Queue, Stack, and [Associative Arrays](https://en.wikipedia.org/wiki/Associative_array) (Often used in the implementation of adjacency lists for graphs)
2. Easy to create a circular list
3. Easy to model real world objects, such as trains, that are sequential
4. Used in separate chaining of certain Hash Table implementations to deal with hashing collisions

## Complexity

| Operation | Singly Linked List | Doubly Linked List |
|-|-|-|
| Search | $O(n)$ | $O(n)$ |
| Insert at head | $O(1)$ | $O(1)$ |
| Insert at tail | $O(1)$ | $O(1)$ |
| Insert in the middle | $O(n)$ | $O(n)$ |
| Delete at head | $O(1)$ | $O(1)$ |
| Delete at tail | $O(n)$ | $O(1)$ |
| Delete in the middle | $O(n)$ | $O(n)$ |

- $n$ is the number of nodes.
- Peeking(=getting an index) from a linked list takes linear time as it traverses from head to tail.
- Deleting a node in the middle of a linked list requires finding the node's previous node.
  - It is why deletion at the tail in a singly linked list takes linear time since it should traverse from head to tail to find the previous node.
  - But, a doubly linked list does not have to do that where the tail node has the pointer to its previous node, so it is possible to access the previous node in constant time.

# Implementation

The two classes have a common interface but perform slightly different operations depending on the class.

<div>
{% plantuml %}
skinparam ClassAttributeIconSize 0
class ListNode {
    +data  :object
}
abstract class LinkedList {
    +empty()  :bool 
    +size()  :int 
    +index(object)  :int 
    +search_by_index(int)  :ListNode 
    +search(object)  :ListNode
    +insert_at_head(object)  :None
    +insert_at_tail(object)  :None
    +insert(int, object)  :None
    +delete_at_head()  :ListNode 
    +delete_at_tail()  :ListNode
    +delete(int)  :ListNode
    +iterate()  :list[object]
}
LinkedList -r-* ListNode
class SllNode {
    +next  :ListNode 
}
class SinglyLinkedList {
    -_size  :int
    +head  :SllNode
    +tail  :SllNode
}
SllNode -u-|> ListNode
SinglyLinkedList -u-|> LinkedList
SinglyLinkedList --> "*" SllNode
class DllNode {
    +prev  :ListNode
    +next  :ListNode
}
class DoublyLinkedList {
    -_size  :int 
    +head  :DllNode
    +tail  :DllNode
}
DllNode -u-|> ListNode
DoublyLinkedList -u-|> LinkedList
DoublyLinkedList --> "*" DllNode
{% endplantuml %}
</div>

- [Source Code](https://github.com/robin-kkk/practical-python/tree/main/dsa/linked_list)

## Singly Linked List

### Search

It is simple to traverse a linked list from the first to the last node just by following the next pointer of each node.

{% highlight python linenos %}
class SinglyLinkedList(LinkedList):

    def __init__(self) -> None:
        self._size = 0
        self.head = None
        self.tail = None

    def search(self, data: object) -> ListNode:
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return None

    # Must guarantee to return None if a given index is outside the boundary.
    def search_by_index(self, at: int) -> ListNode:
        node = self.head
        for i in range(self._size):
            if i == at:
                return node
            node = node.next
        return None
{% endhighlight %}

### Insertion

Notice that we should update the pointers of the two nodes.
- A new node
- The previous node of the node at position we want to add

<div>
{% plantuml %}
frame "1" as first {
    card prev1 [
        <b>at - 1
        ====
        next
        ----
        data
    ]
    card current1 [
        <b>at
        ====
        next
        ----
        data
    ]
    card next1 [
        <b>at + 1
        ====
        next
        ----
        data
    ]
    card new1 #palegreen [
        <b>New
        ====
        next
        ----
        data
    ]
    prev1 -r-> current1
    current1 -r-> next1
    current1 -d- new1 #line:white
}
frame "2" as second {
    card prev2 [
        <b>at - 1
        ====
        next
        ----
        data
    ]
    card current2 [
        <b>at
        ====
        next
        ----
        data
    ]
    card next2 [
        <b>at + 1
        ====
        next
        ----
        data
    ]
    card new2 #palegreen [
        <b>New
        ====
        next
        ----
        data
    ]
    prev2 -r-> current2
    current2 -r-> next2
    new2 -u-> current2 #line:green;line.bold
}
frame "3" as third {
    card prev3 [
        <b>at - 1
        ====
        next
        ----
        data
    ]
    card current3 [
        <b>at
        ====
        next
        ----
        data
    ]
    card next3 [
        <b>at + 1
        ====
        next
        ----
        data
    ]
    card new3 #palegreen [
        <b>New
        ====
        next
        ----
        data
    ]
    current3 -r-> next3
    prev3 -d-> new3 #line:green;line.bold
    new3 -u-> current3 #line:green;line.bold
}
first -r- second #line:white
second -r- third #line:white
{% endplantuml %}
</div>

{% highlight python linenos %}
class SinglyLinkedList(LinkedList):
    # ...

    def insert(self, at: int, data: object) -> None:
        if at > self._size:
            raise Exception(f"cannot insert at index {at}.")

        node = SllNode(data)
        if at == 0:
            # Insert at head.
            if self.head is None:
                self.head, self.tail = node, node
            else:
                node.next = self.head
                self.head = node
        elif at == self._size:
            # Insert at tail.
            self.tail.next = node
            self.tail = node
        else:
            # Insert in the middle.
            prev_node = self.search_by_index(at - 1)
            node.next = prev_node.next
            prev_node.next = node

        self._size += 1
        return None
{% endhighlight %}

### Deletion

<div>
{% plantuml %}
frame "1" as first {
    card prev1 [
        <b>at - 1
        ====
        next
        ----
        data
    ]
    card current1 [
        <b>at
        ====
        next
        ----
        data
    ]
    card next1 [
        <b>at + 1
        ====
        next
        ----
        data
    ]
    prev1 -r-> current1
    current1 -r-> next1
}
frame "2" as second {
    card prev2 [
        <b>at - 1
        ====
        next
        ----
        data
    ]
    card current2 [
        <b>at
        ====
        next
        ----
        data
    ]
    card next2 [
        <b>at + 1
        ====
        next
        ----
        data
    ]
    prev2 -> next2 #line:green;line.bold
    prev2 -r-> current2 #line:white
    current2 -r-> next2
}
frame "3" as third {
    card prev3 [
        <b>at - 1
        ====
        next
        ----
        data
    ]
    card current3 #tomato [
        <b>at
        ====
        next
        ----
        data
    ]
    card next3 [
        <b>at + 1
        ====
        next
        ----
        data
    ]
    prev3 -r-> next3 #line:green;line.bold
    prev3 -u-> current3 #line:white
    current3 -u-> next3 #line:white
}
first -r- second #line:white
second -r- third #line:white
{% endplantuml %}
</div>

{% highlight python linenos %}
class SinglyLinkedList(LinkedList):
    # ...

    def delete(self, at: int) -> ListNode:
        if at >= self._size:
            raise Exception(f"cannot delete at index {at}.")

        deleted = None
        if at == 0:
            # Delete at head.
            if self.head == self.tail:
                self.tail = None
            deleted = self.head
            self.head = deleted.next
        else:
            # Delete at tail or in the middle.
            prev_node = self.search_by_index(at - 1)
            deleted = prev_node.next
            prev_node.next = deleted.next
            if deleted == self.tail:
                self.tail = prev_node
        deleted.reset()
        self._size -= 1
        return deleted
{% endhighlight %}

## Doubly Linked List

### Search

Finding a specific node more quickly than in a singly linked list is interesting
because a doubly linked list can traverse nodes backward.
- If a given index is less than half the number of nodes, then iterate over nodes from the head node.
- Otherwise, iterate over nodes from the tail node reversely.

{% highlight python linenos %}
class DoublyLinkedList(LinkedList):

    def __init__(self) -> None:
        self._size = 0
        self.head = None
        self.tail = None

    def search_by_index(self, at: int) -> ListNode:
        if at < self._size // 2:
            node = self.head
            for i in range(self._size):
                if i == at:
                    return node
                node = node.next
        elif at < self._size:
            node = self.tail
            for i in range(self._size - 1, 0, -1):
                if i == at:
                    return node
                node = node.prev
        return None

    # Same as a singly linked list.
    def search(self, data: object) -> ListNode:
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return None
{% endhighlight %}

### Insertion

To insert a new node, we should change the pointers of the three nodes below.
- The node at position we want to add
- The previous node of the node
- A new node

<div>
{% plantuml %}
frame "1" as first {
    card prev1 [
        <b>at - 1
        ====
        prev
        ----
        next
        ----
        data
    ]
    card current1 [
        <b>at
        ====
        prev
        ----
        next
        ----
        data
    ]
    card next1 [
        <b>at + 1
        ====
        prev
        ----
        next
        ----
        data
    ]
    card new1 #palegreen [
        <b>New
        ====
        prev
        ----
        next
        ----
        data
    ]
    prev1 <-r-> current1
    current1 <-r-> next1
    current1 -d- new1 #line:white
}
frame "2" as second {
    card prev2 [
        <b>at - 1
        ====
        prev
        ----
        next
        ----
        data
    ]
    card current2 [
        <b>at
        ====
        prev
        ----
        next
        ----
        data
    ]
    card next2 [
        <b>at + 1
        ====
        prev
        ----
        next
        ----
        data
    ]
    card new2 #palegreen [
        <b>New
        ====
        prev
        ----
        next
        ----
        data
    ]
    prev2 <-r-> current2
    current2 <-r-> next2
    new2 -u-> prev2 #line:green;line.bold
    new2 -u-> current2 #line:green;line.bold
}
frame "3" as third {
    card prev3 [
        <b>at - 1
        ====
        prev
        ----
        next
        ----
        data
    ]
    card current3 [
        <b>at
        ====
        prev
        ----
        next
        ----
        data
    ]
    card next3 [
        <b>at + 1
        ====
        prev
        ----
        next
        ----
        data
    ]
    card new3 #palegreen [
        <b>New
        ====
        prev
        ----
        next
        ----
        data
    ]
    prev3 <-r- current3
    current3 <-r-> next3
    new3 <-u-> prev3 #line:green;line.bold
    new3 -u-> current3 #line:green;line.bold
}
frame "4" as fourth {
    card prev4 [
        <b>at - 1
        ====
        prev
        ----
        next
        ----
        data
    ]
    card current4 [
        <b>at
        ====
        prev
        ----
        next
        ----
        data
    ]
    card next4 [
        <b>at + 1
        ====
        prev
        ----
        next
        ----
        data
    ]
    card new4 #palegreen [
        <b>New
        ====
        prev
        ----
        next
        ----
        data
    ]
    current4 <-r-> next4
    new4 <-u-> prev4 #line:green;line.bold
    new4 <-u-> current4 #line:green;line.bold
}
first -r- second #line:white
third -r- fourth #line:white
{% endplantuml %}
</div>

{% highlight python linenos %}
class DoublyLinkedList(LinkedList):
    # ...

    def insert(self, at: int, data: object) -> None:
        if at > self._size:
            raise Exception(f"cannot insert at index {at}.")

        node = DllNode(data)
        if at == 0:
            # Insert at head.
            if self.head is None:
                self.head, self.tail = node, node
            else:
                self.head.prev = node
                node.next = self.head
                self.head = node
        elif at == self._size:
            # Insert at tail.
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            # Insert in the middle.
            prev_node = self.search_by_index(at - 1)
            node.next = prev_node.next
            node.prev = prev_node
            prev_node.next.prev = node
            prev_node.next = node
        self._size += 1
        return None
{% endhighlight %}

### Deletion

<div>
{% plantuml %}
frame "1" as first {
    card prev1 [
        <b>at - 1
        ====
        prev
        ----
        next
        ----
        data
    ]
    card current1 [
        <b>at
        ====
        prev
        ----
        next
        ----
        data
    ]
    card next1 [
        <b>at + 1
        ====
        prev
        ----
        next
        ----
        data
    ]
    prev1 <-r-> current1
    current1 <-r-> next1
}
frame "2" as second {
    card prev2 [
        <b>at - 1
        ====
        prev
        ----
        next
        ----
        data
    ]
    card current2 [
        <b>at
        ====
        prev
        ----
        next
        ----
        data
    ]
    card next2 [
        <b>at + 1
        ====
        prev
        ----
        next
        ----
        data
    ]
    prev2 <-r- current2
    current2 <-r-> next2
    prev2 -> next2 #line:green;line.bold
}
frame "3" as third {
    card prev3 [
        <b>at - 1
        ====
        prev
        ----
        next
        ----
        data
    ]
    card current3 [
        <b>at
        ====
        prev
        ----
        next
        ----
        data
    ]
    card next3 [
        <b>at + 1
        ====
        prev
        ----
        next
        ----
        data
    ]
    prev3 <-r- current3
    current3 -r-> next3
    prev3 <-> next3 #line:green;line.bold
}
frame "4" as fourth {
    card prev4 [
        <b>at - 1
        ====
        prev
        ----
        next
        ----
        data
    ]
    card current4 #tomato [
        <b>at
        ====
        prev
        ----
        next
        ----
        data
    ]
    card next4 [
        <b>at + 1
        ====
        prev
        ----
        next
        ----
        data
    ]
    prev4 -d- current4 #line:white
    current4 -u- next4 #line:white
    prev4 <-> next4 #line:green;line.bold
}
first -r- second #line:white
third -r- fourth #line:white
{% endplantuml %}
</div>

{% highlight python linenos %}
class DoublyLinkedList(LinkedList):
    # ...

    def delete(self, at: int) -> ListNode:
        if at > self._size:
            raise Exception(f"cannot insert at index {at}.")

        deleted = None
        if at == 0:
            deleted = self.head
            if self.head == self.tail:
                self.tail = None
            self.head = deleted.next
            if self.head:
                self.head.prev = None
        elif at == self._size - 1:
            deleted = self.tail
            self.tail = deleted.prev
            if self.tail:
                self.tail.next = None
        else:
            # Delete in the middle.
            deleted = self.search_by_index(at)
            deleted.prev.next = deleted.next
            deleted.next.prev = deleted.prev
        deleted.reset()
        self._size -= 1
        return deleted
{% endhighlight %}

# Application

## Linked List vs. Dynamic Array

A [dynamic array](https://en.wikipedia.org/wiki/Dynamic_array) is a data structure that allocates all elements contiguously in memory,
and keeps a count of the current number of elements.
If the space reserved for the array is exceeded, a new greater space is reallocated and elements in an old space are copied,
which is a highly expensive operation.

Note that a number $n$ is the number of entities (elements or nodes) in a data structure.

### Time Complexity

| Operation | Dynamic Array | Doubly Linked List |
|-|-|-|
| Construction | $O(n)$ | $O(1)$ |
| Peek(Indexing) at the beginning | $O(1)$ | $O(1)$ |
| Peek(Indexing) at the end | $O(1)$ | $O(1)$ |
| Peek(Indexing) in the middle | $O(1)$ | $O(n)$ |
| Insert/Delete at the beginning | $O(n)$ | $O(1)$ |
| Insert/Delete at the end | $O(n)$ | $O(1)$ |
| Insert/Delete in the middle | $O(n)$ | $O(n)$ |

- For construction, it is natural to assign a fixed-size of array at first while a linked list starts with the head and tail node.
- For peeking, random access in the array is possible due to indices, which are different from a linked list that does not have an index.
- For insertion and deletion, moving elements behind the inserted or deleted element in the array is inevitable.
However, the linked list does not have to do that; it just needs the change of pointers. 
Nevertheless, in the linked list, we first need to search for the previous node of the node at the position we insert or delete,
which takes linear time.

### Space Complexity

Both take $O(n)$ space, but its storing ways are different.

In terms of memory space, it's good to read [the comparison between array and list in Python](https://www.geeksforgeeks.org/python-lists-vs-numpy-arrays/).

## Leetcode

- See [my list](https://leetcode.com/list/p1j6e151).
