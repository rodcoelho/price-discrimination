#!/usr/bin/env python3

import os

dir_location = "/Users/rodrigocoelho/projects/final-project/worker-nodes/data"
dir = os.listdir(dir_location)

for item in dir:
    if item.endswith(".txt"):
        os.remove(os.path.join(dir_location, item))

