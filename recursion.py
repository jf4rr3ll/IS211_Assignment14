#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 14 Module"""


def fibonacci(n):

    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def gcd(a, b):

    while b > 0:
        (a, b) = (b, (a % b))
    return a


def stringcomparison(s1, s2):

    if len(s1) < len(s2):
        return len(s1) - len(s2)
    if len(s2) < len(s1):
        return len(s1) - len(s2)
    if len(s1) == len(s2):
        return 0
