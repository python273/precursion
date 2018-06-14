# -*- coding: utf-8 -*-
"""
@author: python273
@contact: https://python273.pw
@license: MIT License, see LICENSE file

Copyright (C) 2018
"""

from functools import wraps


def precurse(fn):
    """ Decorator for recursive functions (actually generators)

    >>> @precurse
    ... def sumrange(x):
    ...     if x == 0:
    ...         raise StopIteration(0)
    ...
    ...     r = yield sumrange.r(x - 1)
    ...     raise StopIteration(x + r)
    >>> print(sumrange(1000))
    500500
    """

    @wraps(fn)
    def wrapped(*args, **kwargs):
        stack = []

        gen = fn(*args, **kwargs)
        result = None

        while True:
            try:
                new_gen = gen.send(result)
                result = None
                stack.append(gen)
                gen = new_gen
            except StopIteration as e:
                result = e.args

                if type(result) is tuple and len(result) == 1:
                    result = result[0]

                if stack:
                    gen = stack.pop()
                else:
                    break

        return result

    wrapped.r = fn
    return wrapped
