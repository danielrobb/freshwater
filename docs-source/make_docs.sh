#!/bin/zsh

make clean
cd ../
sphinx-apidoc -f -o docs-source/source freshwater/
cd docs-source/
sphinx-build -b html source ../docs/
make html
touch ../docs/.nojekyll
