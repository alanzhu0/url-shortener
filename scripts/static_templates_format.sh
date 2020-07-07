#!/bin/bash
cd "$(dirname -- "$(dirname -- "$(readlink -f -- "$0")")")" || exit

# Remove trailing whitespace for all JS/CSS/SCSS/txt/JSON/SVG static files
find shortener/static -name vendor -prune -o -type f '(' -name '*.js' -o -name '*.css' -o -name '*.txt' -o -name '*.svg' ')' -exec sed -i 's/\s\+$//' '{}' ';'
# Remove trailing whitespace for all templates
find shortener/templates -type f -exec sed -i 's/\s\+$//' '{}' ';'