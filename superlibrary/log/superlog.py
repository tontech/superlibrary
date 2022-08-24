# AUTHOR: nmacatangay

from datetime import datetime
from datetime import timedelta
import os
import inspect
import subprocess


def test():
    print "test inside superlog"

def initialize_logger(directory, filename):

    # DEFINE FILE DIRECTORY
    full_directory = "%s/%s" % (os.getcwd(), directory)

    # CREATE DIRECTORY IF DIRECTORY DOES NOT YET EXIST
    if not os.path.exists(directory):
        os.makedirs(directory)

    # DEFINE FILE LOCATION
    full_filepath = "%s/%s" % (full_directory, filename)

    # OPEN FILE HANDLE
    global file_handle
    file_handle = open(full_filepath, "a+")

    return None

def infolog(log_type, log_message):

    # DEFINE TIME
    now = (datetime.utcnow() + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")

    # GET STACK
    stack = inspect.stack()

    # FILE WHERE INFOLOG WAS CALLED
    stack_file = stack[1][1].split("/")[-1]

    # FUNCTION OF THE FILE WHERE INFOLOG WAS CALLED
    stack_function = stack[1][3]

    # LINE NUMBER OF FUNCTION OF THE FILE WHERE INFOLOG WAS CALLED
    stack_line_number = stack[1][2]

    # PREPEND TIMESTAMP AND LOG TYPE
    message = "[%s][%s][%s][%s][%s] %s" % (now, stack_file, stack_function, stack_line_number, log_type, log_message)

    # WRITE TO FILE
    if file_handle is not None:
        file_handle.write("%s\n" % message)
    print message

    return None

def echolog(log_message):

    # DEFINE TIME
    now = (datetime.utcnow() + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")

    # GET STACK
    stack = inspect.stack()

    # FILE WHERE INFOLOG WAS CALLED
    stack_file = stack[1][1].split("/")[-1]

    # LINE NUMBER OF FUNCTION OF THE FILE WHERE INFOLOG WAS CALLED
    stack_line_number = stack[1][2]

    # PREPEND TIMESTAMP AND LOG TYPE
    message = "[%s][%s][%s] %s" % (now, stack_file, stack_line_number, log_message)

    # ECHO!
    subprocess.call([ "echo", message ])

    return None
