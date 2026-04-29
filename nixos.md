# Nixos

1. nix-search-cli (Fastest Package Search) This is a dedicated CLI that indexes
   nixpkgs locally for instant searches.
   - Command: nix-search <query>

2. manix (Documentation Search) It searches options, packages, and documentation
   for NixOS, Home Manager, and Flakes.

- Command: manix <query>
- Example: manix services.nginx

3. nh (Already Installed) nh has a search feature built-in which is very handy.

- Command: nh search <query>

4. home-manager (Built-in) If you have home-manager installed as a CLI tool:

- Command: home-manager packages (lists all)
- Command: home-manager option <query> (search options)
