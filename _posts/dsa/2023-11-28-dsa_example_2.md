---
layout: post
title: hi there
date: 2023-11-28
description: this is description
comments: true
tags: dsa
---

> Table of Contents
> * [Concept](#concept)
> * [Implementation](#implementation)
> * [Application](#application)

This post is just `template` file.

# Concept

TBD

# Implementation

TBD

{% highlight c++ linenos %}
// This is comment
int main(int argc, char const *argv[])
{
    string myString;

    cout << "input a string: ";
    getline(cin, myString);
    int length = myString.length();

    char charArray = new char * [length];

    charArray = myString;
    for(int i = 0; i < length; ++i){
        cout << charArray[i] << " ";
    }

    return 0;
}
{% endhighlight %}

## Complexity

| Time | Space |
|------|-------|
| X    | Y     |

# Application

TBD

