import re
import urllib
import urllib2
import csv
import json

def clean_json(json):
    '''
    Turn dirty State Department JSON into clean JSON.
    '''
    return re.sub(r'new Date\(.*?\)', '""', json)

## dict for the get request -- contains search parameters
data = {
    "searchText": "(*) AND (benghazi)", 
    "beginDate": "false",
    "endDate": "false",
    "collection": "false",
    "postedBeginDate": "false",
    "postedEndDate": "false",
    "caseNumber": "F-2014-20439", 
    "collectionMatch": "false",
    "page": 1,
    "start": 0,
    "limit": 9999, 
}

## base url for the get request
url = "https://foia.state.gov/searchapp/Search/SubmitSimpleQuery?"

## url encode the data dictionary and then concatenate it with 
req = urllib2.urlopen( url + urllib.urlencode(data) ).read()
clean = clean_json(req)
results = json.loads(clean)


print ("API Request: " + url + urllib.urlencode(data))


print ("Results returned: " + str(results['totalHits']))


for email in results['Results']:
    
    print(email)
    print(email['subject'])
    print(email['pdfLink'])