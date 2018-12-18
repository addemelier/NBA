import sqlite3
from sqlite3 import Error
import os
import pandas as pd

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

##Some tests to see the tables and if the database relations are working.

def select_all_NBAGame(conn):
    """
    Query all rows in the timeseries table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM NBAGame")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = "c:/Users/adrien_d/Documents/NBAProject/NBA.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query all NBAGame")
        select_all_NBAGame(conn)

if __name__ == '__main__':
    main()
