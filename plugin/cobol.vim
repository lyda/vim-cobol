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

function! LoadCobolPython()
  if !exists('g:cobol_py_loaded')
    exec 'py3file ' . s:path . '/cobol.py'
    let g:cobol_py_loaded = 1
  endif
endfunction

function! Renumber()
  py3 cobol_Renumber()
endfunction

function! Unnumber()
  py3 cobol_Unnumber()
endfunction

call LoadCobolPython()
command! -nargs=0 Renumber call Renumber()
command! -nargs=0 Unnumber call Unnumber()
