#!/usr/bin/python

import sys

from data_analysis.streamer import TwitterStreaming

content = []

if len(sys.argv) > 1:
    with open(sys.argv[1]) as f:
        content = f.readlines()

        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]

# Run
i = TwitterStreaming()
i.start(keyword_filter=content)
