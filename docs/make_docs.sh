#!/bin/zsh

make clean
cd ../
sphinx-apidoc -f -o docs/source freshwater/
cd docs/
sphinx-build -b html source build
make html
touch build/html/.nojekyll
