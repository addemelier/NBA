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


def create_NBAGame(conn, NBAGame):
    """
    Create a new Game into the NBAGame table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO NBAGame('game_id', 'data_set', 'date', 'a1', 'a2', 'a3', 'a4', 'a5', 'h1', 'h2','h3',
    'h4', 'h5', 'period', 'away_score', 'home_score','remaining_time', 'elapsed', 'play_length', 'play_id', 'team',
    'event_type', 'assist', 'away', 'home', 'block', 'entered', 'left','num', 'opponent', 'outof', 'player', 'points',
    'possession', 'reason','result', 'steal', 'type', 'shot_distance', 'original_x', 'original_y','converted_x',
    'converted_y', 'description')
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, NBAGame)

    return cur.lastrowid

def main():
    database = "c:/Users/adrien_d/Documents/NBAProject/NBA.db"
    df = pd.read_csv('[2018-01-22]-0021700692-CHI@NOP.csv')

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        for key in df.groupby(['game_id', 'data_set', 'date', 'a1', 'a2', 'a3', 'a4', 'a5', 'h1', 'h2','h3',
                               'h4', 'h5', 'period', 'away_score', 'home_score','remaining_time', 'elapsed',
                               'play_length', 'play_id', 'team','event_type', 'assist', 'away', 'home', 'block',
                               'entered', 'left','num', 'opponent', 'outof', 'player', 'points','possession',
                               'reason','result', 'steal', 'type', 'shot_distance', 'original_x', 'original_y',
                               'converted_x', 'converted_y', 'description']).groups.keys():
            NBAGame = key;
            NBAGame_id = create_NBAGame(conn, NBAGame)

if __name__ == '__main__':
    main()
