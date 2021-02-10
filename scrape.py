import googlemaps
import pprint

import time
import pickle

import os

# praise GOD for vim
# formatted from a random list I found online
state_capitals = [
    (32.361538, -86.279118),
    (58.301935,-134.419740),
    (33.448457,-112.073844),
    (34.736009,-92.331122),
    (38.555605,-121.468926),
    ( 39.7391667,-104.984167),
    (41.767, -72.677),
    (39.161921,-75.526755),
    (30.4518, -84.27277),
    (33.76,-84.39),
    (21.30895,-157.826182),
    (43.613739, -116.237651),
    (39.783250, -89.650373),
    (39.790942,-86.147685),
    (41.590939,-93.620866),
    (39.04,-95.69),
    (38.197274,-84.86311),
    (30.45809, -91.140229),
    (44.323535,-69.765261),
    (38.972945,-76.501157),
    (42.2352,-71.0275),
    (42.7335,-84.5467),
    (44.95, -93.094),
    (32.320,-90.207),
    (38.572954,-92.189283),
    (46.595805,-112.027031),
    (40.809868, -96.675345),
    (39.160949,-119.753877),
    (43.220093,-71.549127),
    (40.221741,-74.756138),
    (35.667231,-105.964575),
    (42.659829,-73.781339),
    (35.771,-78.638),
    (48.813343,-100.779004),
    (39.962245, -83.000647),
    (35.482309, -97.534994),
    (44.931109,-123.029159),
    (40.269789,-76.875613),
    (41.82355,-71.422132),
    (34.000,-81.035),
    (44.367966,-100.336378),
    (36.165,-86.784),
    (30.266667,-97.75),
    (40.7547,-111.892622),
    (44.26639, -72.57194),
    (37.54,-77.46),
    (47.042418,-122.893077),
    (38.349497,-81.633294),
    (43.074722,-89.384444),
    (41.145548,-104.802042),
]

gmaps = googlemaps.Client(key=os.getenv("GMAP_CLIENT"))
totalArr = []

# get the coordinate of each of the state capital
for coords in state_capitals:
    # find drive in movie theatres within the max radius of the state capitals
    places = gmaps.places(query="drive in movie", location=coords, radius=50000)
    try:
        # if there is a next page, then get the token
        nextPage = places['next_page_token']
    except:
        continue
    # not very fast but I didn't really need speed
    totalArr.extend(places['results'])
    index = 0
    pprint.pprint(totalArr)
    # until there is no next page token
    while(nextPage == "" or nextPage == None):
        # had trouble pining google maps more frequently
        time.sleep(5)
        # request with the same params to get the next apge
        places = gmaps.places(query="drive in movie",page_token=nextPage, location=coords, radius=50000)
        totalArr.extend(places['results'])
        try:
            nextPage = places['next_page_token']
        except:
            break
    # dump all data with pickl
    with open("data.pickle", 'wb') as handle:
        pickle.dump(totalArr, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print("finished")
