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

# Deleter la BD si elle existe déjà
request_delete_db = "DROP DATABASE IF EXISTS livres_en_vrac"
cursor.execute(request_delete_db)

# Créer la BD vierge
request_create_db = "CREATE DATABASE livres_en_vrac"
cursor.execute(request_create_db)

#Utiliser la BD
request_use_bd = "USE livres_en_vrac"
cursor.execute(request_use_bd)

# Créer la BD des clients
request_db_clients = "CREATE TABLE Clients(courriel varchar(50), password varchar(20), prenom char(20), nom char(20), adresse varchar(200), date_de_naissance nvarchar(50))"
cursor.execute(request_db_clients)

# Insérer tout les clients dans la base de données
request_clients = """INSERT INTO Clients (courriel, password, prenom, nom, adresse, date_de_naissance) VALUES (%s, %s, %s, %s, %s, %s)"""
cursor.executemany(request_clients, fake_profiles)

# Créer la BD des livres
request_db_livres = "CREATE TABLE Livres(isbn varchar(20), titre varchar(100), auteur char(100), annee_publication int(4), preface varchar(500))"
cursor.execute(request_db_livres)

# Insérer les livres dans la base de données
request_livres = """INSERT INTO Livres (isbn, titre, auteur, annee_publication, preface) VALUES (%s, %s, %s, %s, %s)"""
cursor.executemany(request_livres, books)