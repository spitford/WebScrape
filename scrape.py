#!/usr/bin/python

# import libraries
import sqlite3
import urllib2
import os.path
from bs4 import BeautifulSoup

import DBCreate

if not os.path.exists('pokemon.db'):
    print ("Creating database...")
    DBCreate.create()
else:
    print ("Database exists...")

db = sqlite3.connect('pokemon.db')
print ("Opened database sucessfully for write")

dex = 0
count = 0
name = ''
type1 = ''
type2 = ''
hp = 0
attack = 0
defense = 0
sattack = 0
sdefense = 0
speed = 0

# specify the url
quote_page = 'https://serebii.net/pokemon/all.shtml'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
name_box = soup.findAll('td', attrs={'class': 'fooinfo'})

for tag in name_box:
    count += 1
    data = tag.text.strip()
    if count % 11 == 3:
        name = data

    if count % 11 == 4:
        types = str(tag).split(" ")
        type1 = types[5][22:types[5].find(".")].capitalize()
        try:
            type2 = types[9][22:types[9].find(".")].capitalize()
        except:
            type2 = ""

    if count % 11 == 6:
        hp = data
    if count % 11 == 7:
        attack = data
    if count % 11 == 8:
        defense = data
    if count % 11 == 9:
        sattack = data
    if count % 11 == 10:
        sdefense = data
    if count % 11 == 0:
        speed = data
        dex += 1

        # print name, type1, type2, hp, attack, defense, sattack, sdefense, speed
        try:
            db.execute("INSERT INTO MASTER (ID,NAME,TYPE1,TYPE2,HP,ATTACK,DEFENSE,SATTACK,SDEFENSE,SPEED) \
                               VALUES (?,?,?,?,?,?,?,?,?,?);",(dex,name,type1,type2,hp,attack,defense,sattack,sdefense,speed))
        except:
            print ("Pokemon " + name + " already added to database")
print (name + " was the final pokemon added to the database")
db.commit()
db.close()
