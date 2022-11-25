set nocompatible              " be improved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" Added plugins

" Color scheme gruvebox
Plugin 'morhetz/gruvbox'
" Indentation to conforming PEP8
Plugin 'vim-scripts/indentpython.vim'
" Syntax checking with flake8
Plugin 'nvie/vim-flake8'
" File browsing with NERDTree
Plugin 'scrooloose/nerdtree'
" Super Search
Plugin 'kien/ctrlp.vim'
" Asynchronous Lint Engine
Plugin 'dense-analysis/ale'


" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

" Put your non-Plugin stuff after this line

" additional set up for grovebox
autocmd vimenter * ++nested colorscheme gruvbox
set background=dark
 
" Specify where vim splits should occur
set splitbelow
set splitright

" split navigations
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>


" Python specific settings
au BufNewFile,BufRead *.py
    \ set tabstop=4 |
    \ set softtabstop=4 |
    \ set shiftwidth=4 |
    \ set textwidth=79 |
    \ set expandtab |
    \ set autoindent |
    \ set fileformat=unix

" other specific settings
au BufNewFile,BufRead *.js, *.html, *.css, *.md
    \ set tabstop=2
    \ set softtabstop=2
    \ set shiftwidth=2

" additional settings
set encoding=utf-8
let python_highlight_all=1
syntax on
set relativenumber
set number
set colorcolumn=79
highligh ColorColumn ctermbg=238
