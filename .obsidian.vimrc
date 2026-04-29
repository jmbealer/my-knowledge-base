" # better use of arrow keys, number increment/decrement
nnoremap <up> <C-a>
nnoremap <down> <C-x>

" # Better page down and page up
noremap <C-n> <C-d>
noremap <C-p> <C-b>


" #mappings
g:mapleader = " "
noremap <leader>fs :write!<cr>
noremap <leader>qq :quit!<cr>
noremap <leader>qa :quitall!<cr>

noremap <leader>ot :term<cr>

noremap <leader>ws <c-w>h
noremap <leader>wt <c-w>j
noremap <leader>wn <c-w>k
noremap <leader>wb <c-w>l

noremap <leader>wd <c-w>q
noremap <leader>wv <c-w>v
noremap <leader>wh <c-w>s

noremap <leader>wrs :vertical resize -2<cr>
noremap <leader>wrt :resize +2<cr>
noremap <leader>wrn :resize -2<cr>
noremap <leader>wrb :vertical resize +2<cr>



    " # make Y consitent with D and C (yank til end)
    map Y y$


    " # disable search highlighting with <C-L> when refreshing screen
    nnoremap <C-L> :nohl<CR><C-L>


" Options
set autowrite
set clipboard=unnamedplus
set completeopt=menu,menuone,noselect
set conceallevel=2
set confirm
set cursorline
set expandtab
set foldlevel=99
set foldmethod=indent
set formatoptions=jcroqlnt
set grepformat=%f:%l:%c:%m
set grepprg=rg\ --vimgrep
set ignorecase
set laststatus=3
set linebreak
set list
set mouse=a
set number
set pumblend=10
set pumheight=10
set relativenumber
set noruler
set scrolloff=4
set sessionoptions=buffers,curdir,tabpages,winsize,help,globals,skiprtp,folds
set shiftround
set shiftwidth=2
set shortmess+=W
set shortmess+=I
set shortmess+=c
set shortmess+=C
set noshowmode
set sidescrolloff=8
set signcolumn=yes
set smartcase
set smartindent
set spelllang=en
set splitbelow
set splitright
set tabstop=2
set termguicolors
set timeoutlen=300
set undofile
set undolevels=10000
set updatetime=200
set virtualedit=block
set wildmode=longest:full,full
set winminwidth=5
set nowrap
