__author__ = 'Wisse'
import sys
import re
import os
from bs4 import BeautifulSoup as bs

# input
folder = sys.argv[1]

# collect the right files/paths
reviews = []

for subdir, dirs, files in os.walk(folder):
    for file in files:
        if file == 'all.review':
            rev = subdir + '/' + file
            reviews.append(rev)

# parse with beautiful soup, write review_text to file
corpus = open('data/sorted_data/parsed.txt', 'w')
for rev in reviews:
    with open(rev, 'r') as infile:
        parse = bs(infile)
        for text in parse.find_all('review_text'):
            corpus.write(text.get_text().encode('ascii', 'ignore'))
        infile.close()

corpus.close()