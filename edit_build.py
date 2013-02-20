#!/usr/bin/env python

import os
import re
from glob import glob
from shutil import move, rmtree

html_files = glob('build/*.html')

for html in html_files:
    prefix, ext = os.path.splitext(html)
    bak = prefix + '.bak'
    move(html, bak)
    with open(bak, 'rU') as f, open(html, 'w') as out:
        for line in f:
            # link to relative html files, images, and static files
            line, no = re.subn(r'/(contact|publications|about)/',
                               '\g<1>.html',
                               line)
            line, no = re.subn(r'/(static|media)', '\g<1>', line)
            # path to homepage
            line, no = re.subn(r'href="/"', 'href="/~cjrogers"', line)
            out.write(line)
    # clean up
    os.remove(bak)

# remove admin dir
admin_media = os.path.join('build', 'static', 'admin')
if os.path.isdir(admin_media):
    rmtree(admin_media)
