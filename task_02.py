#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Task 02 week 12"""


class CustomError(Exception):
    """A Custom Exception"""
    def __init__(self, message, cause):
        Exception.__init__(self, message, cause)
        self.message = message
        self.cause = cause
