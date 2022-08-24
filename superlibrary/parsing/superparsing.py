# AUTHOR: nmacatangay

import simplejson as json

def pretty_print(data):

    # CONVERT TO PRETTY PRINTED JSON
    pretty_print = json.dumps(
            data,
            sort_keys=True,
            indent=4,
            separators=(',', ': '))

    return pretty_print

def two_decimals(data): return "%.2f" % data

def convert_values_to_percentage(dictionary):

    # GET SUM OF VALUES (VALUES MUST BE INT)
    sum_of_values = sum(dictionary.itervalues())

    # COMPUTE PERCENTAGES
    converted_dictionary = {}
    for key in dictionary.keys():
        if int(sum_of_values) == 0:
            converted_dictionary[key] = "0.00"
        else:
            converted_dictionary[key] = two_decimals(((float(dictionary[key]) / float(sum_of_values)) * 100))

    return converted_dictionary

def get_progess(current, total):

    # COMPUTE PERCENTAGE
    progress = "%s%%" % two_decimals(((float(current) / float(total)) * 100))

    return progress

def is_present(dictionary, key):

    # VALIDATE IF VALUES ARE PRESENT
    if dictionary is not None and key is not None:
        if key in dictionary and dictionary[key] is not None:
            return True

    return False

def convert_values_to_string(dictionary,to_float=0):

    return_dict = {}
    
    for dict_data in dictionary:

        if to_float:
            return_dict[dict_data] = float(dictionary[dict_data])
        else:
            return_dict[dict_data] = two_decimals(float(dictionary[dict_data]))

    return return_dict
    

