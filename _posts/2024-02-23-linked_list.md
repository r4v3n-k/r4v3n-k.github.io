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

SinglyLinkedList "many" --> "1" SllNode

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

DoublyLinkedList "many" --> "1" DllNode
{% endplantuml %}

- [Implementation of both lists in detail](https://github.com/robin-kkk/practical-python/tree/main/dsa/linked_list)

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

Notice that what we should do is just to update the pointers of both the node at position we want to add and a new node.

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
    current2 -d- new2 #line:white
    new2 -u-> next2 #line:green;line.bold
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
    prev3 -r-> current3
    current3 -r-> next3 #line:white
    current3 -d- new3 #line:white
    new3 -u-> next3 #line:green;line.bold
    current3 -d-> new3 #line:green;line.bold
}

first -r- second #line:white
second -r- third #line:white
{% endplantuml %}

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

{% highlight python linenos %}
class SinglyLinkedList(LinkedList):
    # ...

    def delete_at_head(self) -> ListNode:
        if self.head is None:
            raise Exception("list must not be empty.")

        if self.head == self.tail:
            self.tail = None
        deleted = self.head
        self.head = self.head.next
        deleted.reset()
        self._size -= 1
        return deleted

    def delete_at_tail(self) -> ListNode:
        if self.tail is None:
            raise Exception("list must not be empty.")

        if self.head == self.tail:
            self.head = None
        deleted = self.tail
        prev_node = self.search_by_index(self._size - 2)
        self.tail = prev_node
        if self.tail:
            self.tail.next = None
        deleted.reset()
        self._size -= 1
        return deleted

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

It is interesting to find a specific node more quickly than in a singly linked list
because a doubly linked list can traverse nodes backwards.
- Iterate over nodes from the head node if a given index is less than half the number of nodes.
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
    current2 -d- new2 #line:white
    new2 -u-> next2 #line:green;line.bold
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
    prev3 <-r-> current3
    current3 -r-> next3
    current3 -d- new3 #line:white
    new3 <-u-> next3 #line:green;line.bold
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
    prev4 <-r-> current4
    current4 -r- next4 #line:white
    current4 -d- new4 #line:white
    new4 <-u-> next4 #line:green;line.bold
    current4 <-d-> new4 #line:green;line.bold
}

first -r- second #line:white
third -r- fourth #line:white
{% endplantuml %}

{% highlight python linenos %}
class DoublyLinkedList(LinkedList):
    # ...

    def insert_at_head(self, data: object) -> None:
        node = DllNode(data)
        if self.head is None:
            self.head, self.tail = node, node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self._size += 1
        return None

    def insert_at_tail(self, data: object) -> None:
        node = DllNode(data)
        if self.tail is None:
            self.head, self.tail = node, node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self._size += 1
        return None

    def insert(self, at: int, data: object) -> None:
        if at > self._size:
            raise Exception(f"cannot insert at index {at}.")

        if at == 0:
            return self.insert_at_head(data)
        elif at == self._size:
            return self.insert_at_tail(data)

        # Insert in the middle.
        node = DllNode(data)
        prev_node = self.search_by_index(at - 1)
        node.next = prev_node.next
        node.prev = prev_node
        prev_node.next.prev = node
        prev_node.next = node
        self._size += 1
        return None
{% endhighlight %}

### Deletion

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

{% highlight python linenos %}
class DoublyLinkedList(LinkedList):
    # ...

    def delete_at_head(self) -> ListNode:
        if self.head is None:
            raise Exception("list must not be empty.")

        if self.head == self.tail:
            self.tail = None
        deleted = self.head
        self.head = deleted.next
        if self.head:
            self.head.prev = None
        deleted.reset()
        self._size -= 1
        return deleted

    def delete_at_tail(self) -> ListNode:
        if self.tail is None:
            raise Exception("list must not be empty.")

        if self.head == self.tail:
            self.head = None
        deleted = self.tail
        self.tail = deleted.prev
        if self.tail:
            self.tail.next = None
        deleted.reset()
        self._size -= 1
        return deleted

    def delete(self, at: int) -> ListNode:
        if at > self._size:
            raise Exception(f"cannot insert at index {at}.")

        if at == 0:
            return self.delete_at_head()
        elif at == self._size - 1:
            return self.delete_at_tail()

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

Time and Space Complexity

Why?

## Reverse

TBD

## ZigZag

TBD

## Leetcode

TBD
