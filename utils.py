from requests.adapters import HTTPAdapter, Retry
import requests
import json

session = requests.Session()

retries = Retry(total=10, backoff_factor=30, status_forcelist=[500, 502, 503, 504])

session.mount('http://', HTTPAdapter(max_retries=retries))


# get the data from the guild website
def get_data(url):
    r = session.get(url)
    return r.json()

# save the data to a file
def save_formatted_data(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)

# save a dictionary to csv file
def save_dictionary_to_csv(dictionary, filename):
    # we want to print the csv in the format of: key, value
    with open(filename, 'w') as f:
        # write the headers, election ID and title
        f.write("Election ID,Title\n")
        for key in dictionary.keys():
            f.write("%s,%s\n" % (key, dictionary[key]))