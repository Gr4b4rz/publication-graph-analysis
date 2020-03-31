import os
import json
import xplore

FILE = open("wut-publications.json", "w")
API_KEY = os.getenv("IEEE_XPLORE_API_KEY") # read env variable
YEARS = [2017, 2018, 2019, 2020]
AFFILATION = "Warsaw University of Technology"
MAX_POSSIBLE_RESULTS = 200

data = []
for year in YEARS:
    query = xplore.xploreapi.XPLORE(API_KEY)
    query.affiliationText(AFFILATION)
    query.publicationYear(year)
    query.maximumResults(MAX_POSSIBLE_RESULTS)
    data.append(query.callAPI())

with open('wut-publications.json', 'w') as outfile:
    json.dump(data, outfile)
