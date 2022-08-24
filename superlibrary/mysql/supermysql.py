#!/usr/bin/python

# AUTHOR: Mildred Cabuyao

import MySQLdb

def connect_to_mysqldb(host, database, username, password):

    # CONNECTION STRING
    conn = MySQLdb.connect(host=host,user =username, passwd = password, db =database)
    cursor = conn.cursor()

    return [conn, cursor]

def disconnect_from_mysqldb(conn, cursor):

    cursor.close()
    conn.close()

    return None

def create_database(cursor, database, user='', password='', host=''):

    # create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS %s" % database)

    # create user and password for specific database
    if user and password and host:
        cursor.execute("GRANT ALL ON %s.* TO '%s'@'%s' IDENTIFIED BY '%s'" % (database, user, host,password))

    return None

def mysql_execute(cursor,query_string):

    # create table
    cursor.execute(query_string)

    return None

