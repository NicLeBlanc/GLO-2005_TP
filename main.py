import pymysql.cursors
from data import fake_profiles
from data import books

connection = pymysql.connect(
    host="127.0.0.1",
    user="root123",
    password="123",
    db="livres_en_vrac",
    autocommit=True
)

cursor = connection.cursor()

# Permet d'insérer tout les clients dans la base de données
request_clients = """INSERT INTO Clients (courriel, password, prenom, nom, adresse, date_de_naissance) VALUES (%s, %s, %s, %s, %s, %s)"""
cursor.executemany(request_clients, fake_profiles)

# Permet d'insérer les livres dans la base de données
request_livres = """INSERT INTO Livres (isbn, titre, auteur, annee_publication, preface) VALUES (%s, %s, %s, %s, %s)"""
cursor.executemany(request_livres, books)