import pymysql.cursors
from data import fake_profiles
from data import books
from data import fake_seller
from data import securise

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

#/*
#* Création des tables entités
#*/

request_db_clients = "CREATE TABLE Clients(courriel varchar(50), PRIMARY KEY(courriel), prenom char(20), nom char(20), adresse varchar(200), date_de_naissance nvarchar(50))"
cursor.execute(request_db_clients)

request_db_vendeurs = "CREATE TABLE Vendeurs(ID varchar(20),PRIMARY KEY(ID), prenom char(20), nom char(20), adresse varchar(200), pays_origine char(20), courriel_vendeur varchar(50), cote_global integer(1))"
cursor.execute(request_db_vendeurs)

request_db_livres = "CREATE TABLE Livres(isbn varchar(20), PRIMARY KEY(isbn), titre varchar(100), auteur char(100), annee_publication int(4), preface varchar(500))"
cursor.execute(request_db_livres)

request_db_genre = "CREATE TABLE Genres(type varchar(20), PRIMARY KEY(type))"
cursor.execute(request_db_genre)

request_db_commande = "CREATE TABLE Commandes(ID varchar(20), PRIMARY KEY(ID), niveau_satisfaction integer(1), prix_total float(12), date_expedition nvarchar(50), date_commande nvarchar(50))"
cursor.execute(request_db_commande)

#/*
#* Création des tables relations
#*/

request_securise = "CREATE TABLE Securise(courriel varchar(50), password varchar(50), PRIMARY KEY (courriel), FOREIGN KEY (courriel) REFERENCES Clients(courriel) ON UPDATE CASCADE ON DELETE RESTRICT)"
cursor.execute(request_securise)

request_prefere = "CREATE TABLE Prefere(courriel varchar(50), type varchar(20), PRIMARY KEY (courriel), FOREIGN KEY (courriel) REFERENCES Clients(courriel) ON UPDATE CASCADE ON DELETE RESTRICT, FOREIGN KEY (type) REFERENCES Genres(type) ON UPDATE CASCADE ON DELETE RESTRICT)"
cursor.execute(request_prefere)

request_evalue = "CREATE TABLE Evalue(courriel varchar(50), ID varchar(20), cote integer(1), PRIMARY KEY (courriel), FOREIGN KEY (courriel) REFERENCES Clients(courriel) ON UPDATE CASCADE ON DELETE RESTRICT, FOREIGN KEY (ID) REFERENCES Vendeurs(ID) ON UPDATE CASCADE ON DELETE RESTRICT)"
cursor.execute(request_evalue)

request_vend = "CREATE TABLE Vend(ID varchar(20), isbn varchar(20), nbr_exemplaire integer(4), prix float(8), PRIMARY KEY (ID), FOREIGN KEY (ID) REFERENCES Vendeurs(ID) ON UPDATE CASCADE ON DELETE RESTRICT, FOREIGN KEY (isbn) REFERENCES Livres(isbn) ON UPDATE CASCADE ON DELETE RESTRICT)"
cursor.execute(request_vend)

request_classer = "CREATE TABLE Classer(isbn varchar(20), type varchar(20), PRIMARY KEY (isbn), FOREIGN KEY (isbn) REFERENCES Livres(isbn) ON UPDATE CASCADE ON DELETE RESTRICT, FOREIGN KEY (type) REFERENCES Genres(type) ON UPDATE CASCADE ON DELETE RESTRICT)"
cursor.execute(request_classer)

request_contient = "CREATE TABLE Contient(ID varchar(20), isbn varchar(20), nbr_exemplaire integer(4), PRIMARY KEY (ID), FOREIGN KEY (ID) REFERENCES Vendeurs(ID) ON UPDATE CASCADE ON DELETE RESTRICT, FOREIGN KEY (isbn) REFERENCES Livres(isbn) ON UPDATE CASCADE ON DELETE RESTRICT)"
cursor.execute(request_contient)

#/*
#* Insertion dans les tables
#*/

# Les tables avec un *** dans la description sont à rajouter à la database - LCC

# Insérer tout les clients dans la base de données
request_clients = """INSERT INTO Clients (courriel, prenom, nom, adresse, date_de_naissance) VALUES (%s, %s, %s, %s, %s)"""
cursor.executemany(request_clients, fake_profiles)

# # Insérer les vendeurs dans la base de données *** fake_vendeur
# request_vendeur = """INSERT INTO Vendeur (ID, nom, courriel_vendeur, adresse, pays_origine) VALUES(%s, %s, %s, %s, %s)"""
# cursor.executemany(request_vendeur, fake_seller)

# Insérer les livres dans la base de données
request_livre = """INSERT INTO Livres (isbn, titre, auteur, annee_publication, preface) VALUES (%s, %s, %s, %s, %s)"""
cursor.executemany(request_livre, books)

# # Insérer les genres dans la base de données *** genre
# request_genre = """INSERT INTO Genre (type) VALUES(%s)"""
# cursor.executemany(request_genre, genre)
#
# # Insérer les commandes dans la base de données *** fake_commande
# request_commande = """INSERT INTO Commande (ID, niveau_satisfaction, prix_total, date_expedition, date_commande) VALUES (%s, %s, %s, %s, %s)"""
# cursor.executemany(request_commande, fake_commande)
#
# Insérer la relation Securise dans la base de données *** securise

request_securise = """INSERT INTO Securise (courriel, password) VALUES (%s, %s)"""
cursor.executemany(request_securise, securise)
#
# # Insérer la relation prefere dans la base de données *** prefere
#
# request_prefere = """INSERT INTO Prefere(courriel, courriel, genre) VALUES (%s, %s, %s)"""
# cursor.executemany(request_prefere, prefere)
#
# # Insérer la relation evalue dans la base de données *** evalue
#
# request_evalue = """INSERT INTO Evalue(courriel, ID, cote) VALUES (%s, %s, %s)"""
# cursor.executemany(request_evalue, evalue)
#
# # Insérer la relation vend dans la base de données *** vend
#
# request_vend = """INSERT INTO Vend(ID, isbn, nbr_exemplaire, prix) VALUES (%s,%s,%s,%s)"""
# cursor.executemany(request_vend, vend)
#
# # Insérer la relation classer dans la base de données *** classer
#
# request_classer = """INSERT INTO Classer(isbn, type, livre, Genre) VALUES (%s, %s, %s, %s)""" #type est en orange, j'ignore pourquoi LCC
# cursor.executemany(request_classer, classer)
#
# # Insérer la relation contient dans la base de données *** contient
#
# request_contient = """INSERT INTO Contient(ID, isbn, nbr_exemplaire)"""
# cursor.executemany(request_contient, contient)

def select_books():
    request = "SELECT * FROM Livre ORDER BY annee_publication DESC LIMIT 0,10;"
    cursor.execute(request)
    books = [entry[0] for entry in cursor.fetchall()]
    return books