# AUTHOR: nmacatangay

import requests
import simplejson as json

def get_total_rows(url, port, database, design, view, key):

    # DEFINE URL
    if key is None:
        url = "http://%s:%s/%s/_design/%s/_view/%s" % (url, port, database, design, view)
    else:
        url = "http://%s:%s/%s/_design/%s/_view/%s?key=\"%s\"" % (url, port, database, design, view, key)

    # EXECUTE GET REQUEST
    result = requests.get(url)

    # CONVERT TO JSON
    json_data = result.json()

    actual_rows = len(json_data["rows"]) 

    return actual_rows

def get_all_data(url, port, database, design, view, key, limit, skip):

    # DEFINE URL
    if key is None:
        url = "http://%s:%s/%s/_design/%s/_view/%s?limit=%s&skip=%s" % (url, port, database, design, view, limit, skip)
    else:
        url = "http://%s:%s/%s/_design/%s/_view/%s?key=\"%s\"&limit=%s&skip=%s" % (url, port, database, design, view, key, limit, skip)

    # EXECUTE GET REQUEST
    result = requests.get(url)

    # CONVERT TO JSON
    json_data = result.json()

    # GET VALUE
    rows = json_data["rows"]

    return rows
