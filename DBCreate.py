#!/usr/bin/python

import sqlite3

def create():

    conn = sqlite3.connect('pokemon.db')
    print ("Opened database successfully")

    conn.execute('''CREATE TABLE MASTER
                (ID INT PRIMARY KEY     NOT NULL,
                NAME            TEXT    NOT NULL,
                TYPE1           TEXT    NOT NULL,
                TYPE2           TEXT,
                HP              INT     NOT NULL,
                ATTACK          INT     NOT NULL,
                DEFENSE         INT     NOT NULL,
                SATTACK         INT     NOT NULL,
                SDEFENSE        INT     NOT NULL,
                SPEED           INT     NOT NULL);''')

    print ("Table created successfully")

    conn.close()

if __name__ == '__main__':
    create()
