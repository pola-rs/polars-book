#!/bin/bash

wget https://github.com/RuneStar/name-cleanup-2014/releases/download/1.1/name-cleanup-2014.zip -O data/runescape.zip
unzip -p data/runescape.zip > data/runescape.csv

wget https://files.pushshift.io/reddit/69M_reddit_accounts.csv.gz -O data/reddit.gz
gunzip -c data/reddit.gz > data/reddit.csv

