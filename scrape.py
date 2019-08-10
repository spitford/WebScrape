# import libraries
import sqlite3
import urllib2
from bs4 import BeautifulSoup

count = 0
name = ''
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
        print name, hp, attack, defense, sattack, sdefense, speed
