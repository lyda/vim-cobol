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
import math

def cobol_Renumber():
  if vim.current.buffer.options['filetype'] == 'cobol':
    gap = {}
    last_line_no = 0
    lines = vim.current.buffer
    for i in range(len(lines)):
      if len(lines[i]) == 0 or lines[i][:6] == '      ':
        if not gap:
          gap['i'] = i
          gap['last_line_no'] = last_line_no
      else:
        try:
          last_line_no = int(lines[i][:6])
        except ValueError:
            print('Malformed line - has non-numbers in columns 1-6')
            return
        if gap:
          delta = math.floor((last_line_no - gap['last_line_no']) /
            (i - gap['i'] + 1))
          if delta > 1:
            new_line_no = gap['last_line_no'] + delta
            for j in range(gap['i'], i):
              lines[j] = ('%06d' % new_line_no) + lines[j][6:]
              new_line_no += delta
            gap = {}
    if gap:
      delta = 100
      new_line_no = gap['last_line_no'] + delta
      for j in range(gap['i'], len(lines)):
        lines[j] = ('%06d' % new_line_no) + lines[j][6:]
        new_line_no += delta
  else:
    print('Not a COBOL file. This is a %s file.' %
        vim.current.buffer.options['filetype'].decode('UTF-8'))

def cobol_Unnumber():
  if vim.current.buffer.options['filetype'] == 'cobol':
    lines = vim.current.buffer
    for i in range(len(lines)):
      if lines[i][:6].isdigit():
        lines[i] = '      ' + lines[i][6:]
  else:
    print('Not a COBOL file. This is a %s file.' %
        vim.current.buffer.options['filetype'].decode('UTF-8'))
