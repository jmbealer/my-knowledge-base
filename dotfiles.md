# Dotfiles

I'm going to using chezmoi to manage my dotfiles. I'm also thinking about
ansibe, but I'm not sure yet.

What is chezmoi?

- chezmoi is a cli tool that manage your dotfiles across multiple machines,
  securely.

install chezmoi

initalize chezmoi: chezmoi init

add a file to chezmoi: chezmoi add ~/.bashrc
unlink a file from anisble: unlink ~/.bashrc

edit the source state: chezmoi edit ~/.bashrc

see changes chezmoi would make: chezmoi diff

apply changes: chezmoi -v apply

has verbose flag: chezmoi -v
has dry run flag: chezmoi -n

chezmoi cd # cd to chezmoi source directory
