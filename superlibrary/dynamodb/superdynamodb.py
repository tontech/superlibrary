# AUTHOR: nmacatangay

import boto.dynamodb2
from boto.dynamodb2.table import Table
import time

def connect_to_amazon(region, key, secret):

    # CONNECT TO AMAZON DYNAMODB
    amazon = boto.dynamodb2.connect_to_region(
            region,
            aws_access_key_id=key,
            aws_secret_access_key=secret
    )

    return amazon

def connect_to_dynamo(name, amazon):

    # CONNECT TO AMAZON DYNAMODB TABLE
    table = Table(name, connection=amazon)

    return table

def modify_throughput(table, read, write):

    # COMMENT ME
    #return None

    # GET TABLE INFORMATION
    table_data = table.describe()

    # ONLY CHANGE IF READ OR WRITE IS DIFFERENT
    if read != table_data["Table"]["ProvisionedThroughput"]["ReadCapacityUnits"] or write != table_data["Table"]["ProvisionedThroughput"]["WriteCapacityUnits"]:

        forever = True
        while forever:

            # ONLY UPDATE IF TABLE STATUS IS ACTIVE
            if table_data["Table"]["TableStatus"] == "ACTIVE":

                # UPDATE AMAZON DYNAMODB TABLE THROUGHPUT
                try:
                    table.update(throughput={
                        'read': read,
                        'write': write,
                    })
                except boto.exception.JSONResponseError:
                    # LIMIT EXCEEDED
                    forever = False

                # GET OUT OF LOOP
                forever = False

            else:

                # TRY AGAIN AFTER 5 SECONDS
                time.sleep(5)
                table_data = table.describe()

        forever = True
        while forever:

            # RETURN ONLY AFTER STATUS IS ACTIVE (WAIT TIL THROUGHPUT UPDATE IS DONE)
            table_data = table.describe()

            # ONLY UPDATE IF TABLE STATUS IS ACTIVE
            if table_data["Table"]["TableStatus"] == "ACTIVE":

                # GET OUT OF LOOP
                forever = False


    return None

def data_exists(table, hash_key, range_key, hash_value, range_value):

    return table.has_item(**{
            hash_key: hash_value,
            range_key: range_value})

def insert_to_dynamo(table, data):

    table.put_item(data=data)

    return None

def dynamo_query(table, hash_key_condition, hash_value, range_key_condition, range_value):

    # DYNAMO DB QUERY
    results = table.query_2(**{
        hash_key_condition: hash_value,
        range_key_condition: range_value})

    return results

def dynamo_query_all(table, hash_key_condition, hash_value):

    # DYNAMO DB QUERY
    results = table.query_2(**{hash_key_condition: hash_value})

    return results

def dynamo_to_dict(table_results):

    # DECLARE RETURN VALUE
    dictionary_array = []

    # GO THROUGH ALL RESULTS
    for table_result in table_results:

        # DECLARE EMPTY VARIABLE
        dictionary = {}

        # CREATE DICTIONARY
        for key in table_result.keys():
            if table_result[key] is None:
                dictionary[key] = None
            else:
                dictionary[key] = table_result[key]

        # PUSH CREATED DICTIONARY TO RETURN VALUE
        dictionary_array.append(dictionary)

    return dictionary_array
