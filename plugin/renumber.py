#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Kevin Lyda <kevin@phrye.com>
#
# Distributed under terms of the GPL license.

"""
COBOL utilities.
"""

import vim

print(vim.current.buffer.name)
b = vim.current.buffer
for i in range(len(b)):
  b[i] = 'moo ' + b[i]
