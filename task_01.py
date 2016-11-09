#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 Week 12"""


class BaseError(Exception):
    """A Basic Exception Class"""
    pass


class StringError(BaseError, TypeError):
    """Exception for Strings"""
    pass


class NumberError(BaseError, TypeError):
    """Exception for Numbers"""
    pass


class NonZeroError(NumberError):
    """Exception for NonZeros"""
    pass
