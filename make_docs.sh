#!/bin/zsh
rm -r *.js *.html *.inv _static _source
cp ../../README.rst source/readme.rst
make clean
cd ../../
sphinx-apidoc -f -o docs/docs/source freshwater/
cd docs/docs/
sphinx-build -b html source build
make html
cp -r build/html/* ../
