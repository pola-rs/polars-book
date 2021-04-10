#!/bin/bash

mkdir "data"
wget https://github.com/ritchie46/static/releases/download/0.0.1/reddit100k.tar.gz -O data/reddit.tar.gz
tar -xf data/reddit.tar.gz -O > data/reddit.csv

wget https://github.com/ritchie46/static/releases/download/0.0.1/runescape100k.tar.gz -O data/runescape.tar.gz
tar -xf data/runescape.tar.gz -O > data/runescape.csv
