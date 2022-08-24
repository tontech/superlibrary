# AUTHOR: nmacatangay

from datetime import datetime
from datetime import timedelta
import time

def get_timestamp():

    # GET DATE IN YYYY-MM-DD HH:MM:SS FORMAT
    timestamp = (datetime.utcnow() + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")

    return timestamp

def get_timestamp_v2():

    # GET DATE IN YYYY-MM-DD HH:MM:SS FORMAT
    timestamp = (datetime.utcnow() + timedelta(hours=8)).strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    return timestamp

def get_today():

    # GET DATE IN YYYY-MM-DD FORMAT
    today = (datetime.utcnow() + timedelta(hours=8)).strftime("%Y-%m-%d")

    return today

def get_yesterday():

    # GET DATE IN YYYY-MM-DD FORMAT
    yesterday = (datetime.utcnow() + timedelta(hours=8) - timedelta(hours=24)).strftime("%Y-%m-%d")

    return yesterday

def get_epochtime(date):

    # GET EPOCHTIME FROM YYYY-MM-DD date format
    sp_date = date.split("-")
    epochtime = (datetime(int(sp_date[0]), int(sp_date[1]), int(sp_date[2]), 0, 0) - datetime(1970, 1, 1)).total_seconds()

    return epochtime

def parse_epochtime(epoch_date):

    # CONVERT EPOCHTIME TO YYYY-MM-DD date format
    parsed_date = time.strftime("%Y-%m-%d", time.gmtime(int(epoch_date)))

    return parsed_date

def get_epochdatetime(date, time):

    # GET EPOCHTIME FROM YYYY-MM-DD HH:MM:SS date format
    epochtime = (datetime.strptime("%s %s" % (date, time), "%Y-%m-%d %H:%M:%S") - datetime(1970, 1, 1)).total_seconds()

    return epochtime

def parse_date(date):

    # PARSE DATE
    if date == "ALL":
        date = None
    elif date == "TODAY":
        date = get_today()
    elif date == "YESTERDAY":
        date = get_yesterday()

    return date

def time_to_sec(time):

    l = time.split(':')

    return int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])

def sec_to_time(secs):

    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)

    return '%02d:%02d:%02d' % (hours, mins, secs)
