#!/usr/bin/python
import sys

from hippo_data_analysis.streamer import TwitterStreaming

content = []

if len(sys.argv) > 1:
    with open(sys.argv[1]) as f:
        content = f.readlines()

        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]

# Run
streamer = TwitterStreaming()
streamer.start(keyword_filter=content)
