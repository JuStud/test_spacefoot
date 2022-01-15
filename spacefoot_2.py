import requests
import json
from mysql.connector import (connection)
import csv

page = "https://api.spacefoot.com/api/jobs"

r = requests.get(page)

data = r.text

parsed = json.loads(data)

# print(json.dumps(parsed, indent=4))
offre = []

for i in parsed:

    title = i['title']
    content = i['content']
    date = i['publishedAt']
    type = i['contract_type']['name']
    team = i['team']['name']

    for p in i['locations']:
        if len(i['locations']) > 1:
            x = i['locations']
            lieux = ''
            for locs in x:
                lieux = lieux + locs['name'] + ' '
        else:
            lieux = p['name']

    row = [title, type, team, lieux, date, content]
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
