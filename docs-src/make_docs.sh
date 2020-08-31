#!/bin/zsh
cp ../README.rst readme.rst
make clean
cd ../
sphinx-apidoc -f -o docs-src/ freshwater/
cd docs-src/
sphinx-build -b html . _build
make html
cp -r _build/html/* ../docs/

