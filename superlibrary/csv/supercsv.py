#!/usr/bin/python

# AUTHOR: Mildred Cabuyao

import csv

def csv_read(file_path):

    with open(file_path, 'rb') as f:
        reader = csv.reader(f)
        data = list(reader)

    return data

