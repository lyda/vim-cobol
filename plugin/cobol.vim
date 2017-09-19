" cobol.vim - Some useful COBOL scripts.
" Maintainer:   Kevin Lyda <kevin@phrye.com>
" Version:      0.1
" TODO: add vim-scripts config

if exists('g:loaded_cobol') || &cp
  echo "Already loaded."
  finish
endif
let g:loaded_cobol = 1

if !has('python3')
  echo "Missing python."
  finish
endif

let s:path = fnamemodify(resolve(expand('<sfile>:p')), ':h')

function! HelloWorld()
  exec 'py3file ' . s:path . '/renumber.py'
endfunction
