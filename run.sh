#!/bin/bash

# cd to the directory
cd /home/cogs/Documents/UoB-GoS-Election-Tracker/

# run the script
python get_election_list.py

# check for updates
if [[ `git status --porcelain` ]]; then
    # changes
    git add .
    git commit -m "Update"
    git push
else
    # no changes
    echo "No changes found..."
fi
