precursion [![PyPI](https://img.shields.io/pypi/v/precursion.svg)](https://pypi.org/project/precursion/) ![Python 2.7, 3.4, 3.5, 3.6](https://img.shields.io/pypi/pyversions/precursion.svg)
======
**precursion** – Python module to avoid `RecursionError: maximum recursion depth exceeded` easily

## Usage

Ok, let's write recursive function:
```python
def sumrange(x):
    if x == 0:
        return 0

    r = sumrange(x - 1)
    return x + r

print(sumrange(10)  # 55
```
Pretty simple. But what if we call it with bigger argument
```python
print(sumrange(1000))
# RecursionError: maximum recursion depth exceeded
```
Let's fix it with precursion module:
```python
@precurse
def sumrange(x):
    if x == 0:
        # return was:
        # return 0
        # now we need to use StopIteration exception:
        raise StopIteration(0)

    # recursive call was:
    # r = sumrange(x - 1)
    # now we use yield:
    r = yield sumrange.r(x - 1)
    raise StopIteration(x + r)

print(sumrange(1000))  # 500500!!1
```
That's it!

#### What is `.r` in `sumrange.r`?

It's unwrapped function, so you `yield` unwrapped generator

## Pros and cons:

#### Pros
The code looks cleaner. Yep.

#### Cons
Function calls have performance and memory overhead, so using
the decorator is slower than if you use Tail-call optimization via `while`
or implement a stack inside a function.