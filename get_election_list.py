"""
Get's a list of elections and saves it into a file in the `data` folder
Designed to indicate when new elections have been created on MSL
"""

from notif_utils import *
from utils import *

base_url = "https://www.guildofstudents.com/svc/voting/stats/election/paramstats/" + \
    "?groupIds=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20&sortBy=itemname&sortDirection=ascending"


def get_election_list():
    # initialise a dictionary of election IDs and Titles
    election_list = {}

    print("[INFO] Fetching election list...")

    """
    We currently have no way to distinguish between no access to an election and it not existing
    As a workaround to this, we'll check for 10 failed in a row, at which point we assume that's all of them
    """

    # the number of failed attempts to get an election
    failed_attempts = 0

    # current ID to check
    current_id = 1

    while failed_attempts < 10:
        url = "https://www.guildofstudents.com/svc/voting/stats/election/paramstats/" + \
            str(current_id) + "?groupIds=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20&sortBy=itemname&sortDirection=ascending"

        # get the election data
        data = get_data(url)

        # check if the title is "Unknown"
        if data["Title"] == "Unknown":
            # increment failed attempts
            failed_attempts += 1

            print("[INFO] Failed to get election with ID " +
                  str(current_id) + " (" + str(failed_attempts) + "/10)")

        else:
            # Add the ID and title to the dictionary
            election_list[current_id] = data["Title"]

            if failed_attempts > 0:
                # reset failed attempts
                failed_attempts = 0

                print("[INFO] Reset failed attempts to 0.")

            print("[INFO] Got election with ID " + str(current_id))

        # increment the ID
        current_id += 1

    # save the election list to a json file
    save_formatted_data(election_list, "data/all_elections_active_list.json")

    # save the election list to a csv file
    save_dictionary_to_csv(election_list, "data/all_elections_active_list.csv")

    print("[INFO] Fetching election list... done!")


if __name__ == "__main__":
    get_election_list()

    # send a notification if new election data is found
    if check_for_changes():
        # changes found, send notif
        print("[INFO] Changes found, sending notification...")
        new_election_data()
    else:
        # no changes found
        print("[INFO] No changes found.")