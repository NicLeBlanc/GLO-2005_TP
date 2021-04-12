import hashlib
import pymysql as pymysql
from data import fake_profiles, books, fake_seller, vend, securise_hash, prefere, genres, classer, fake_commandes, \
    passer, contient, evaluation


def init_Database():

# ***************************************************
# *           Connection à la database              *
# ***************************************************

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

    # Utiliser la BD
    request_use_bd = "USE livres_en_vrac"
    cursor.execute(request_use_bd)

    # ***************************************************
    # *         Création des tables entités             *
    # ***************************************************

    request_db_clients = "CREATE TABLE Clients(courriel varchar(50), PRIMARY KEY(courriel), prenom char(20), nom char(20), adresse varchar(200), date_de_naissance nvarchar(50))"
    cursor.execute(request_db_clients)

    request_db_vendeurs = "CREATE TABLE Vendeurs(ID_vendeur varchar(20),PRIMARY KEY(ID_vendeur), nom char(40),courriel_vendeur varchar(50), adresse varchar(200), pays_origine char(50), cote_globale int(1))"
    cursor.execute(request_db_vendeurs)

    request_db_livres = "CREATE TABLE Livres(isbn varchar(20), PRIMARY KEY(isbn), titre varchar(100), auteur char(100), annee_publication int(4), preface varchar(500))"
    cursor.execute(request_db_livres)

    request_db_genre = "CREATE TABLE Genres(type varchar(20), PRIMARY KEY(type))"
    cursor.execute(request_db_genre)

    request_db_commande = "CREATE TABLE Commandes(ID_commande varchar(20), PRIMARY KEY(ID_commande), mode_paiement varchar(20), prix_total float(12), date_commande nvarchar(50), date_expedition nvarchar(50))"
    cursor.execute(request_db_commande)


    # ***************************************************
    # *          Création des tables relations          *
    # ***************************************************

    request_securise = "CREATE TABLE Securise(courriel varchar(50), mot_de_passe nvarchar(150), PRIMARY KEY (courriel), FOREIGN KEY (courriel) REFERENCES Clients(courriel) ON UPDATE CASCADE ON DELETE RESTRICT)"
    cursor.execute(request_securise)

    request_prefere = "CREATE TABLE Prefere(courriel varchar(50), type varchar(20), PRIMARY KEY (courriel), FOREIGN KEY (courriel) REFERENCES Clients(courriel) ON UPDATE CASCADE ON DELETE RESTRICT, FOREIGN KEY (type) REFERENCES Genres(type) ON UPDATE CASCADE ON DELETE RESTRICT)"
    cursor.execute(request_prefere)

    request_evalue = "CREATE TABLE Evalue(courriel varchar(50), ID_vendeur varchar(20), cote_vendeur integer(1), FOREIGN KEY (courriel) REFERENCES Clients(courriel) ON UPDATE CASCADE ON DELETE RESTRICT, FOREIGN KEY (ID_vendeur) REFERENCES Vendeurs(ID_vendeur) ON UPDATE CASCADE ON DELETE RESTRICT)"
    cursor.execute(request_evalue)

    request_vend = "CREATE TABLE Vend(ID_vendeur varchar(20), isbn varchar(20), nbr_exemplaire integer(4), prix float(8), FOREIGN KEY (ID_vendeur) REFERENCES Vendeurs(ID_vendeur) ON UPDATE CASCADE ON DELETE RESTRICT, FOREIGN KEY (isbn) REFERENCES Livres(isbn) ON UPDATE CASCADE ON DELETE RESTRICT)"
    cursor.execute(request_vend)

    request_classer = "CREATE TABLE Classer(isbn varchar(20), type varchar(20), PRIMARY KEY (isbn), FOREIGN KEY (isbn) REFERENCES Livres(isbn) ON UPDATE CASCADE ON DELETE RESTRICT, FOREIGN KEY (type) REFERENCES Genres(type) ON UPDATE CASCADE ON DELETE RESTRICT)"
    cursor.execute(request_classer)

    request_contient = "CREATE TABLE Contient(ID_commande varchar(20), isbn varchar(20), nbr_exemplaire integer(4), FOREIGN KEY (ID_commande) REFERENCES Commandes(ID_commande) ON UPDATE CASCADE ON DELETE RESTRICT, FOREIGN KEY (isbn) REFERENCES Livres(isbn) ON UPDATE CASCADE ON DELETE RESTRICT)"
    cursor.execute(request_contient)

    request_passer = "CREATE TABLE Passer(ID_commande varchar(20), courriel varchar(50), FOREIGN KEY (ID_commande) REFERENCES Commandes(ID_commande) ON UPDATE CASCADE ON DELETE RESTRICT, FOREIGN KEY (courriel) REFERENCES Clients(courriel) ON UPDATE CASCADE ON DELETE RESTRICT)"
    cursor.execute(request_passer)


    # ***************************************************
    # *                 Triggers Pre Insert             *
    # ***************************************************

    request_trigger_Insert_Cote = """ CREATE TRIGGER UpdateCoteGlobaleInsert AFTER INSERT ON Evalue FOR EACH ROW BEGIN UPDATE Vendeurs SET vendeurs.cote_globale = (SELECT AVG (cote_vendeur) from Evalue where new.ID_vendeur = Evalue.ID_vendeur) where Vendeurs.ID_vendeur = new.ID_vendeur; end"""
    cursor.execute(request_trigger_Insert_Cote)


    request_trigger_Update_Cote = """ CREATE TRIGGER UpdateCoteGlobaleUpdate 
    AFTER UPDATE ON Evalue 
    FOR EACH ROW 
    BEGIN UPDATE Vendeur 
    SET vendeur.cote_global = (SELECT AVG (cote) from Evalue where NEW.ID_vendeur = Evalue.ID_vendeur) where vendeur.ID_vendeur = new.ID_vendeur; end"""
    cursor.execute(request_trigger_Update_Cote)


    request_trigger_Insert_prix_total = """CREATE TRIGGER UpdatePrixTotalInsert
    AFTER INSERT ON contient
    FOR EACH ROW
    BEGIN
    UPDATE commandes
    SET commandes.prix_total = (SELECT SUM(c.nbr_exemplaire*v.prix) FROM contient c, Vend v WHERE (c.ID_commande = NEW.ID_commande) AND (c.isbn = v.isbn))
    WHERE NEW.ID_commande = commandes.ID_commande ;END"""
    cursor.execute(request_trigger_Insert_prix_total)


    request_trigger_Update_prix_total = """CREATE TRIGGER UpdatePrixTotalUpdate
    AFTER UPDATE ON contient
    FOR EACH ROW
    BEGIN
    UPDATE commandes
    SET commandes.prix_total = (SELECT SUM(c.nbr_exemplaire*v.prix) FROM contient c, Vend v WHERE (c.ID_commande = NEW.ID_commande) AND (c.isbn = v.isbn))
    WHERE NEW.ID_commande = commandes.ID_commande ;END"""
    cursor.execute(request_trigger_Update_prix_total)


    # ***************************************************
    # *       Insertion dans les tables Entités         *
    # ***************************************************

    request_clients = """INSERT INTO Clients (courriel, prenom, nom, adresse, date_de_naissance) VALUES (%s, %s, %s, %s, %s)"""
    cursor.executemany(request_clients, fake_profiles)

    request_vendeur = """INSERT INTO Vendeurs (ID_vendeur, nom, courriel_vendeur, adresse, pays_origine, cote_globale) VALUES(%s, %s, %s, %s, %s, %s)"""
    cursor.executemany(request_vendeur, fake_seller)

    request_livre = """INSERT INTO Livres (isbn, titre, auteur, annee_publication, preface) VALUES (%s, %s, %s, %s, %s)"""
    cursor.executemany(request_livre, books)

    request_commande = """INSERT INTO Commandes (ID_commande, mode_paiement, prix_total, date_commande, date_expedition) VALUES (%s, %s, %s, %s, %s)"""
    cursor.executemany(request_commande, fake_commandes)

    request_genre = """INSERT INTO Genres (type) VALUES(%s)"""
    cursor.executemany(request_genre, genres)


    # ****************************************************
    # *      Insertion dans les tables Relations         *
    # ****************************************************

    request_securise = """INSERT INTO Securise (courriel, mot_de_passe) VALUES (%s, %s)"""
    cursor.executemany(request_securise, securise_hash)

    request_vend = """INSERT INTO Vend(ID_vendeur, isbn, nbr_exemplaire, prix) VALUES (%s,%s,%s,%s)"""
    cursor.executemany(request_vend, vend)

    request_contient = """INSERT INTO Contient(ID_commande, isbn, nbr_exemplaire) VALUES (%s,%s,%s)"""
    cursor.executemany(request_contient, contient)

    request_prefere = """INSERT INTO Prefere(courriel, type) VALUES (%s, %s)"""
    cursor.executemany(request_prefere, prefere)

    request_evalue = """INSERT INTO Evalue(courriel, ID_vendeur, cote_vendeur) VALUES (%s, %s, %s)"""
    cursor.executemany(request_evalue, evaluation)

    request_classer = """INSERT INTO Classer(isbn, type) VALUES (%s, %s)"""
    cursor.executemany(request_classer, classer)

    request_passer = """INSERT INTO Passer(ID_commande, courriel) VALUES (%s, %s)"""
    cursor.executemany(request_passer, passer)

    # ***************************************************
    # *                 Triggers Post Insert            *
    # ***************************************************

    request_trigger_changement_commande = """CREATE TRIGGER BeforeInsertCommande
    BEFORE INSERT ON contient
    FOR EACH ROW 
    BEGIN
    if (SELECT DISTINCT b.nbr_exemplaire FROM (contient a, vend b) WHERE (a.isbn = b.isbn) AND (a.isbn = NEW.isbn)) < NEW.nbr_exemplaire
    THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Vous tentez de commander plus de livres que ce que le stock peut offrir.';
    END IF;
    END """
    cursor.execute(request_trigger_changement_commande)

    request_trigger_changement_commande_update = """CREATE TRIGGER BeforeUpdateCommande
    BEFORE UPDATE ON contient
    FOR EACH ROW 
    BEGIN
    if (SELECT DISTINCT b.nbr_exemplaire FROM (contient a, vend b) WHERE (a.isbn = b.isbn) AND (a.isbn = NEW.isbn)) < NEW.nbr_exemplaire
    THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Vous tentez de commander plus de livres que ce que le stock peut offrir.';
    END IF;
    END """
    cursor.execute(request_trigger_changement_commande_update)

    # ***************************************************
    # *                 Index                           *
    # ***************************************************

    request_index_clients_hash = """CREATE INDEX hash_client ON Clients (courriel) USING HASH"""
    cursor.execute(request_index_clients_hash)

    request_index_securise_hash = """CREATE INDEX hash_securise ON Securise (courriel) USING HASH"""
    cursor.execute(request_index_securise_hash)

    request_index_livre_btree = """CREATE INDEX btree_livres ON Livres (annee_publication) USING BTREE"""
    cursor.execute(request_index_livre_btree)

    request_index_livre_hash = """CREATE INDEX hash_livres ON Livres (Auteur) USING HASH"""
    cursor.execute(request_index_livre_hash)

    request_index_commande_hash = """CREATE INDEX hash_commandes ON Commandes (ID_commande) USING HASH"""
    cursor.execute(request_index_commande_hash)