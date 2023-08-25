"""
Utilities to send specific notifications
"""

from dotenv import load_dotenv
from git import Repo
import requests
import os

# load environment variables
load_dotenv()

# get ntfy topic from environment variables
TOPIC = os.getenv("TOPIC")

def check_for_changes():
    # check if there are changes to the election list
    repo = Repo(".")
    if repo.is_dirty():
        # changes found, return true
        return True
    else:
        # no changes found, return false
        return False


def new_election_data():
    # send a notification indicating how many new shifts are available
    requests.post(
        "https://ntfy.sh/" + TOPIC,
        data = "There are is new election data available!",
        headers = {
            "Title": "New Election Details!",
            "Priority": "4"
        }
    )