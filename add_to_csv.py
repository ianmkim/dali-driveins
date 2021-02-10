import pickle
import pprint

import details

import csv

# load saved data
with open("data.pickle", "rb") as handle:
    data = pickle.load(handle)

metadata = []

index = 0
# writes pickled file to a csv
with open("data_file.csv", "w") as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for business in data:
        # get the business details from google
        detail = details.get_details(business['place_id'])['result']
        metadata.append(detail)
        try:
            print(index)
            index += 1
            # write the business to csv file, with new details
            writer.writerow([business['name'],
                             business['formatted_address'],
                             business['place_id'],
                             business['rating'],
                             detail['formatted_phone_number'],
                             detail['website']])
        except Exception as e:
            # if anything goes wrong, just continue bc who cares
            print(e)
            continue

# save all the metadata so that I don't have to keep pinging google
with open("metadata.pickle", 'wb') as handle:
    pickle.dump(metadata, handle, protocol=pickle.HIGHEST_PROTOCOL)



