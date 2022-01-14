from operator import imod
import requests
from bs4 import BeautifulSoup
from mysql.connector import (connection)
import csv

page = "https://spacefoot.com/jobs"

r = requests.get(page)
soup = BeautifulSoup(r.text, 'html.parser')  # Initialisation de BeautifulSoup

link = []
# Récupération de tous les liens de la page
if r.ok:
    for h2 in soup.findAll('div', attrs={'class': 'box'}):
        title = h2.findAll('a')
        for a in title:
            link.append(a['href'])

newPage = "https://spacefoot.com"
offre = []
# fouille de tous les liens
for i in link:

    post = newPage + i
    r = requests.get(post)
    soup = BeautifulSoup(r.text, 'html.parser')

    if r.ok:
        title = soup.find('h1', attrs={'class': 'title'}).text
        # Recupère les infos de la colonne droite
        for content in soup.findAll('div', attrs={'class': 'box content'}):
            dd = content.findAll('dd')
            if len(dd) > len(content.findAll('dt')):
                type = dd[0].text
                team = dd[1].text
                loc = dd[2].text + ' ' + dd[3].text
                date = dd[4].text
            else :
                type = dd[0].text
                team = dd[1].text
                loc = dd[2].text
                date = dd[3].text
        # Ici on a récupérer le contenu
        for contenu in soup.findAll('div', attrs={'class': 'is-three-quarters'}):
            fiche = contenu.text
        row = [title, type, team, loc, date, fiche]
        offre.append(row)

# On établis la connexion

users = input("Entrer le nom d'utilisateur de la base de données")
pswd = input("Entrer le mot de passe d'accès de la base de données")
hosti = input("Entrer l'adresse de la base de données")
ports = input("Entrer le port de la base de données")
db = input("Entrer le nom de la base de données")

# conn = connection.MySQLConnection(
#     user='root',
#     password='root',
#     host='127.0.0.1',
#     port='8889',
#     database='spacefoot'
# )

conn = connection.MySQLConnection(
    user=users,
    password=pswd,
    host=hosti,
    port=ports,
    database=db
)


mycursor = conn.cursor()

# Insertion dans la base de données

if conn:
    print('Réussie')
    for i in offre:
        req = 'insert into jobs(type, titre, team, localisation, date_publication, contenu) values (%s, %s, %s, %s, %s, %s)'
        val = (i[0], i[1], i[2], i[3], i[4], i[5])
        mycursor.execute(req, val)  
        conn.commit() 

# Select 

if conn:
    team = ['Tech', 'Ebiz', 'Support', 'Design', 'Team SPACEFOOT']
    # open the file in the write mode
    f = open('rapport.csv', 'w')
    # create the csv writer
    writer = csv.writer(f)
    for i in team:
        req = 'select count(*) from jobs where team ="'+i+'";'
        mycursor.execute(req)  
        result = mycursor.fetchone()
        l = result[0]
        # write a row to the csv file
        writer.writerow(['Pour la team '+i+' il existe '+ str(l) +' offre(s)'])
    # close the file
    f.close()


conn.close()
