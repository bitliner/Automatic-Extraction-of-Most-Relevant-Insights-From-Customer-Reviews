__author__ = 'Wisse'

from bs4 import BeautifulSoup as bs
import sys
import os

folder = sys.argv[1]

blogs = []

for subdir, dirs, files in os.walk(folder):
    for file in files:
        blog = subdir + file
        blogs.append(blog)

output = open('data/parsed_blogs.txt', 'w')

for path in blogs:
    with open(path, 'r') as blog:
        print "now processing %s" % blog
        parsed = bs(blog)
        for text in parsed.find_all('post'):
            post = text.get_text().replace("urlLink", '').strip()
            output.write(post.encode('ascii', 'ignore') + '\n')
        blog.close()

output.close()