# AUTHOR: nmacatangay

import psycopg2

def connect_to_database(host, database, username, password):

    # CONNECTION STRING
    conn_string = "host='%s' dbname='%s' user='%s' password='%s'" % (host, database, username, password)
    conn = psycopg2.connect(conn_string)
    conn.autocommit = True
    cursor = conn.cursor()

    return [conn, cursor]

def execute(cursor, sql_statement):

    cursor.execute(sql_statement)

    # HOW TO EXTRACT - FOR REFERENCE ONLY
#   for row in cursor:
#       data1 = row[0]
#       data2 = row[1]

    return cursor

def disconnect_from_database(conn, cursor):

    cursor.close()
    conn.close()

    return None
