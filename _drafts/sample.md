---
layout: post
title: this is a sample
date: 2015-10-20
description: this is description
comments: true
tags: ps ml
---

> Table of Contents
> * [Heading 1](#heading-1)
> * [Formmatting and links](#formmatting-and-links)
> * [Images](#images)
> * [Code block](#code-block)
>    * [Raw](#Raw)
>    * [Syntax highlighting](#syntax-highlighting)
> * [Math](#math)
> * [Highlight](#highlight)


This post is just `template` file.

# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5

# Formmatting and links

Jean shorts raw denim Vice normcore, art party High Life PBR skateboard stumptown vinyl kitsch. Four loko meh 8-bit, tousled banh mi tilde forage Schlitz dreamcatcher twee 3 wolf moon. Chambray asymmetrical paleo salvia, sartorial umami four loko master cleanse drinking vinegar brunch. <a href="https://www.pinterest.com" target="blank">Pinterest</a> DIY authentic Schlitz, hoodie Intelligentsia butcher trust fund brunch shabby chic Kickstarter forage flexitarian. Direct trade <a href="https://en.wikipedia.org/wiki/Cold-pressed_juice" target="blank">cold-pressed</a> meggings stumptown plaid, pop-up taxidermy. Hoodie XOXO fingerstache scenester Echo Park. Plaid ugh Wes Anderson, freegan pug selvage fanny pack leggings pickled food truck DIY irony Banksy.

#### Hipster list
<ul>
    <li>brunch</li>
    <li>fixie</li>
    <li>raybans</li>
    <li>messenger bag</li>
</ul>

Hoodie Thundercats retro, tote bag 8-bit Godard craft beer gastropub. Truffaut Tumblr taxidermy, raw denim Kickstarter sartorial dreamcatcher. Quinoa chambray slow-carb salvia readymade, bicycle rights 90's yr typewriter selfies letterpress cardigan vegan.

<hr>

Pug heirloom High Life vinyl swag, single-origin coffee four dollar toast taxidermy reprehenderit fap distillery master cleanse locavore. Est anim sapiente leggings Brooklyn ea. Thundercats locavore excepteur veniam eiusmod. Raw denim Truffaut Schlitz, migas sapiente Portland VHS twee Bushwick Marfa typewriter retro id keytar.

We do not grow absolutely, chronologically. We grow sometimes in one dimension, and not in another, unevenly. We grow partially. We are relative. We are mature in one realm, childish in another.
—Anais Nin

Fap aliqua qui, scenester pug Echo Park polaroid irony shabby chic ex cardigan church-key Odd Future accusamus. Blog stumptown sartorial squid, gastropub duis aesthetic Truffaut vero. Pinterest tilde twee, odio mumblecore jean shorts lumbersexual.


# Images

Jean shorts raw denim Vice normcore, art party High Life PBR skateboard stumptown vinyl kitsch. Fingerstache four loko meh 8-bit, tousled banh mi tilde forage Schlitz dreamcatcher twee 3 wolf moon. Chambray asymmetrical paleo salvia, sartorial umami four loko master cleanse drinking vinegar brunch.

<div class="img_row">
    <img class="col three" src="{{ site.baseurl }}/assets/img/9.jpg">
</div>
<div class="img_row">
    <img class="col three" src="{{ site.baseurl }}/assets/img/7.jpg">
</div>
<div class="col three caption">
    A simple, elegant caption looks good between image rows, after each row, or doesn't have to be there at all.
</div>
<div class="img_row">
    <img class="col two first" src="{{ site.baseurl }}/assets/img/8.jpg">
    <img class="col one last" src="{{ site.baseurl }}/assets/img/10.jpg">
</div>

Slow-carb four dollar toast Helvetica pop-up. Kale chips next level literally trust fund Pitchfork. Jean shorts Pinterest beard, farm-to-table irony craft beer swag tofu 8-bit Banksy. Quinoa forage fanny pack, pug hashtag Echo Park heirloom Schlitz tote bag artisan Neutra mumblecore 90's shabby chic raw denim.


<div class="img_row">
    <img class="col one first" src="{{ site.baseurl }}/assets/img/11.jpg">
    <img class="col one" src="{{ site.baseurl }}/assets/img/12.jpg">
    <img class="col one last" src="{{ site.baseurl }}/assets/img/7.jpg">
</div>


# Code block

This theme implements a built-in Jekyll feature, the use of Pygments, for sytanx highlighting. It supports more than 100 languages. This example is in C++. All you have to do is wrap your code in a liquid tag:

## Raw

{% raw %}
{% highlight c++ linenos %}  <br/> code code code <br/> {% endhighlight %}
{% endraw %}
Produces something like this:

## Syntax highlighting

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


# Math

This theme supports rendering beautiful math in inline and display modes using [KaTeX](https://khan.github.io/KaTeX/) engine. You just need to surround your math expression as like below.

### Usage

{% highlight terminal %}
    
    $  -> inline mode
    $$ -> display mode
    \$ -> escape mode
    
{% endhighlight %}

Here is an example:

### Non-display mode, Inline mode

$
\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
$

This is a mixed environment where you can have normal text and $c = \pm\sqrt{a^2 + b^2}$ fenced math. \$!

### Display mode

$$
\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
$$

Note that [KaTeX](https://khan.github.io/KaTeX/) is work in progress, so it does not support the full range of math expressions as, say, [MathJax](https://www.mathjax.org/). Yet, it is [blazing fast](http://www.intmath.com/cg5/katex-mathjax-comparison.php).

# Output in terminal

{% highlight terminal %}
    
    Server address: http://127.0.0.1:4000
  Server running... press ctrl-c to stop.
      Regenerating: 1 file(s) changed at 2020-03-06 20:50:46
                    _sass/_code.scss
                    ...done in 3.713741 seconds.

      Regenerating: 1 file(s) changed at 2020-03-06 20:52:55
                    _sass/_code.scss
                    ...done in 3.130828 seconds.

      Regenerating: 1 file(s) changed at 2020-03-06 20:52:59
                    _sass/_code.scss
                    ...done in 4.431754 seconds.
    
{% endhighlight %}

# Gist

{% gist robin-kkk/982e2371ea150b39ba7b9c3be52127dd %}

# PlantUML

{% plantuml %}
skinparam componentStyle uml2
Browser -right-> [Edge]
[Edge] -right-> [Central]
[Central] -right-> [Origin]
{% endplantuml %}

{% plantuml %}
participant Participant as Foo
actor       Actor       as Foo1
boundary    Boundary    as Foo2
control     Control     as Foo3
entity      Entity      as Foo4
database    Database    as Foo5
collections Collections as Foo6
queue       Queue       as Foo7
Foo -> Foo1 : To actor
Foo -> Foo2 : To boundary
Foo -> Foo3 : To control
Foo -> Foo4 : To entity
Foo -> Foo5 : To database
Foo -> Foo6 : To collections
Foo -> Foo7: To queue
{% endplantuml %}
