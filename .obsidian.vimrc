" # better use of arrow keys, number increment/decrement
nnoremap <up> <C-a>
nnoremap <down> <C-x>

" # Better page down and page up
noremap <C-n> <C-d>
noremap <C-p> <C-b>


" #mappings
noremap s b
noremap t j
noremap n k
noremap b w

noremap w s
noremap j t
noremap k n

noremap S B
noremap T }
noremap N {
noremap B W

noremap B B
noremap W S
noremap J T
noremap K N

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

