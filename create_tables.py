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

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = "c:/Users/adrien_d/Documents/NBAProject/NBA.db"


    #Column labels have been surpressed due to confidentiality.
    sql_create_NBAGame_table = """ CREATE TABLE IF NOT EXISTS NBAGame (
                                    game_id str,
                                    play_id str,
                                    data_set str,
                                    date date,
                                    a1 str,
                                    a2 str,
                                    a3 str,
                                    a4 str,
                                    a5 str,
                                    h1 str,
                                    h2 str,
                                    h3 str,
                                    h4 str,
                                    h5 str,
                                    away_score integer,
                                    home_score integer,
                                    remaining_time datetime,
                                    elapsed datetime,
                                    play_length datetime,
                                    team str,
                                    event_type str,
                                    assist str,
                                    away str,
                                    home str,
                                    block str,
                                    entered str,
                                    left str,
                                    num integer,
                                    opponent str,
                                    outof integer,
                                    player str,
                                    points integer,
                                    possession str,
                                    reason str,
                                    result str,
                                    steal str,
                                    type str,
                                    shot_distance integer,
                                    original_x integer,
                                    original_y integer,
                                    converted_x float,
                                    converted_y float,
                                    description str,
                                    period integer,
                                    PRIMARY KEY (game_id, play_id)
                                ); """

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_NBAGame_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
