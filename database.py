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

#/*
#* Création des tables entités
#*/

request_db_clients = "CREATE TABLE Clients(courriel varchar(50), PRIMARY KEY(courriel), prenom char(20), nom char(20), adresse varchar(200), date_de_naissance nvarchar(50))"
cursor.execute(request_db_clients)

request_db_vendeurs = "CREATE TABLE Vendeur(ID varchar(20),PRIMARY KEY(ID), prenom char(20), nom char(20), adresse varchar(200), pays_origin char(20), courriel_vendeur varchar(50), cote_global integer(1))"
cursor.execute(request_db_vendeurs)

request_db_livres = "CREATE TABLE Livre(isbn varchar(20), PRIMARY KEY(isbn), titre varchar(100), auteur char(100), annee_publication int(4), preface varchar(500))"
cursor.execute(request_db_livres)

request_db_genre = "CREATE TABLE Genre(type varchar(20), PRIMARY KEY(type))"
cursor.execute(request_db_genre)

request_db_commande = "CREATE TABLE Commande(ID varchar(20), PRIMARY KEY(ID), niveau_satisfaction integer(1), prix_total float(12), date_expedition nvarchar(50), date_commande nvarchar(50))"
cursor.execute(request_db_commande)

#/*
#* Création des tables relations
#*/

request_securise = "CREATE TABLE Securise(password varchar(50), courriel varchar(50), PRIMARY KEY (courriel), FOREIGN KEY (courriel) REFERENCES Clients(courriel) ON UPDATE CASCADE ON DELETE RESTRICT)"
cursor.execute(request_securise)

request_prefere = "CREATE TABLE Prefere(courriel varchar(50), type varchar(20), PRIMARY KEY (courriel), FOREIGN KEY (courriel) REFERENCES Clients(courriel) ON UPDATE CASCADE ON DELETE RESTRICT, FOREIGN KEY (type) REFERENCES Genre(type) ON UPDATE CASCADE ON DELETE RESTRICT)"
cursor.execute(request_prefere)

request_evalue = "CREATE TABLE Evalue(courriel varchar(50), ID varchar(20), cote integer(1), PRIMARY KEY (courriel), FOREIGN KEY (courriel) REFERENCES Clients(courriel) ON UPDATE CASCADE ON DELETE RESTRICT, FOREIGN KEY (ID) REFERENCES Vendeur(ID) ON UPDATE CASCADE ON DELETE RESTRICT)"
cursor.execute(request_evalue)

request_vend = "CREATE TABLE Vend(ID varchar(20), isbn varchar(20), nbr_exemplaire integer(4), prix float(8), PRIMARY KEY (ID), FOREIGN KEY (ID) REFERENCES Vendeur(ID) ON UPDATE CASCADE ON DELETE RESTRICT, FOREIGN KEY (isbn) REFERENCES Livre(isbn) ON UPDATE CASCADE ON DELETE RESTRICT)"
cursor.execute(request_vend)

request_classer = "CREATE TABLE Classer(isbn varchar(20), type varchar(20), PRIMARY KEY (isbn), FOREIGN KEY (isbn) REFERENCES Livre(isbn) ON UPDATE CASCADE ON DELETE RESTRICT, FOREIGN KEY (type) REFERENCES Genre(type) ON UPDATE CASCADE ON DELETE RESTRICT)"
cursor.execute(request_classer)

request_contient = "CREATE TABLE Contient(ID varchar(20), isbn varchar(20), nbr_exemplaire integer(4), PRIMARY KEY (ID), FOREIGN KEY (ID) REFERENCES Vendeur(ID) ON UPDATE CASCADE ON DELETE RESTRICT, FOREIGN KEY (isbn) REFERENCES Livre(isbn) ON UPDATE CASCADE ON DELETE RESTRICT)"
cursor.execute(request_contient)

#/*
#* Insertion dans les tables
#*/

# Insérer tout les clients dans la base de données
request_clients = """INSERT INTO Clients (courriel, prenom, nom, adresse, date_de_naissance) VALUES (%s, %s, %s, %s, %s)"""
cursor.executemany(request_clients, fake_profiles)

# Insérer les livres dans la base de données
request_livre = """INSERT INTO Livre (isbn, titre, auteur, annee_publication, preface) VALUES (%s, %s, %s, %s, %s)"""
cursor.executemany(request_livre, books)



def select_books():
    request = "SELECT * FROM Livre ORDER BY annee_publication DESC LIMIT 0,10;"
    cursor.execute(request)
    books = [entry[0] for entry in cursor.fetchall()]
    return books