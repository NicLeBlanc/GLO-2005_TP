import pymysql
import hashlib


# ***************************************************
# *                 Fonctions                       *
# ***************************************************

def connection():
    connection = pymysql.connect(
        host="127.0.0.1",
        user="root123",
        password="123",
        db="livres_en_vrac",
        autocommit=True)
    return connection

cursor = connection().cursor()

# /*
# @Affichage des 25 livres les plus récents
# */

def select_books_recent():
    cmd = 'SELECT * FROM Livres ORDER BY annee_publication DESC limit 25;'
    cursor.execute(cmd)
    info = cursor.fetchall()
    return info

# /*
# @Hashage de password
# */

def encrypt_pass(courriel, password):
    salt = str.encode(courriel)
    mot_de_passe = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 10)
    alpha = ""
    for character in str(mot_de_passe):
        if character.isalnum():
            alpha += character
    return alpha

# /*
# @Insertion de nouvelle inscription
# */

def insert_inscription(courriel, prenom, nom, adresse, date_de_naissance):
    request = """INSERT INTO Clients (courriel, prenom, nom, adresse, date_de_naissance) VALUES ("{}","{}","{}","{}","{}");""".format(courriel, prenom, nom, adresse, date_de_naissance)
    cursor.execute(request)

# /*
# @Insertion de mot de passe encryptés
# */

def insert_securise(courriel, mot_de_passe):
    courriel_str = '"' + courriel + '"'
    mot_de_passe_encrypt = encrypt_pass(courriel_str, mot_de_passe)
    request = """INSERT INTO Securise (courriel, mot_de_passe) VALUES ("{}","{}")""".format(courriel, mot_de_passe_encrypt)
    cursor.execute(request)
# /*
# @Insertion de contient lcc
# */

def insert_contient(ID_commande,isbn, nbr_exemplaire):
    request = """INSERT INTO Contient(ID_commande,isbn,nbr_exemplaire) VALUES ("{}","{}","{}");""".format(ID_commande,isbn,nbr_exemplaire)
    cursor.execute(request)

# /*
# @Insertion de l'evaluation dans evalue lcc
# */

def insert_evalue(courriel, ID_vendeur, cote_vendeur):
    request = """INSERT INTO Evalue(courriel, ID_vendeur, cote_vendeur) VALUES ("{}","{}","{}");""".format(courriel, ID_vendeur, cote_vendeur)
    cursor.execute(request)

# /*
# @Insertion de passer lcc
# */

def insert_passer(ID_commande, courriel):
    request = """INSERT INTO Passer(ID_commande, courriel) VALUES ("{}","{}");""".format(ID_commande, courriel)
    cursor.execute(request)

# /*
# @Insertion de commande lcc
# */

def insert_commande(ID_commande, mode_paiement, prix_total, date_commande, date_expedition):
    request = """INSERT INTO Commande(ID_commande, mode_paiement, prix_total, date_commande, date_expedition) VALUES ("{}","{}","{}""{}","{}");""".format(ID_commande, mode_paiement, prix_total, date_commande, date_expedition)
    cursor.execute(request)

# /*
# @Insertion de prefere lcc
# */

def insert_prefere(courriel, type):
    request = """INSERT INTO Prefere(courriel, type) VALUES ("{}","{}");""".format(courriel, type)
    cursor.execute(request)

# /*
# @Courriel existant
# */

def courriel_existant(courriel):
    request = """SELECT COUNT(*) FROM Clients WHERE courriel = "{}";""".format(courriel)
    cursor.execute(request)
    fetch = cursor.fetchall()
    result = (fetch[0][0])
    if result > 0:
        return True
    else:
        return False

# /*
# @Commandes du client
# */

def get_commandes(courriel):
    request = """SELECT * FROM Commandes join Passer on Commandes.ID_commande = Passer.ID_commande WHERE courriel = "{}";""".format(courriel)
    cursor.execute(request)
    return cursor.fetchall()

def get_commandeCourante(courriel):
    request = """SELECT DISTINCT c.ID_commande, c.mode_paiement, c.prix_total, c.date_expedition, c.date_commande
    FROM Commandes c
    left join Passer on c.ID_commande = Passer.ID_commande
    WHERE courriel = "{}";""".format(courriel)
    cursor.execute(request)
    return cursor.fetchall()

def get_commandeContenu(courriel):
    request = """SELECT l.isbn, l.titre, l.auteur, l.annee_publication, d.nbr_exemplaire, v.prix
    FROM Commandes c
    LEFT JOIN Passer p on c.ID_commande = p.ID_commande
    LEFT JOIN Contient d on c.ID_commande = d.ID_commande
    LEFT JOIN Livres l on d.isbn = l.isbn
    LEFT JOIN Vend v on l.isbn = v.isbn
    WHERE courriel = "{}";""".format(courriel)
    cursor.execute(request)
    return cursor.fetchall()


# /*
# @Livres recommandés selon les goûts
# */

def get_preferences(courriel):
    request = """SELECT livres.isbn, titre, auteur, annee_publication, vend.prix FROM Livres JOIN Classer on Classer.isbn = Livres.isbn JOIN Prefere on Classer.type = Prefere.type JOIN Vend on Livres.isbn = Vend.isbn WHERE Prefere.courriel = "{}";""".format(courriel)
    cursor.execute(request)
    return cursor.fetchall()

# /*
# @Livres recommandés selon les goûts
# */
def get_pref(courriel):
    request = """SELECT type FROM prefere WHERE courriel = "{}";""".format(courriel)
    cursor.execute(request)
    return cursor.fetchall()

# /*
# @Recherche de livres
# */
def select_books(type_recherche, recherche):
    request = """ SELECT * from Livres JOIN Vend on Livres.isbn = Vend.isbn JOIN Vendeurs on Vend.ID_vendeur = Vendeurs.ID_vendeur WHERE Livres.{} LIKE "%{}%";""".format(type_recherche, recherche)
    cursor.execute(request)
    books = cursor.fetchall()
    return books

# /*
# @Trouver la dernière commande passée
# */
def last_order():
    request_get_last_order = "SELECT ID_commande FROM Commandes ORDER BY CAST(ID_commande as DECIMAL) DESC LIMIT 1;"
    cursor.execute(request_get_last_order)
    last_order_num_raw = cursor.fetchone()
    last_order_num_filter = int(last_order_num_raw[0])
    last_order_num = last_order_num_filter + 1
    return str(last_order_num)

# /*
# @Créer une nouvelle commande
# */
def create_new_odrder(email, id_commande):
    request_insert_commande = "INSERT INTO Commandes (ID_commande, mode_paiement, prix_total, date_commande, date_expedition) VALUES ({}, null, 0, null, null);".format(id_commande)
    cursor.execute(request_insert_commande)
    request_insert_passer = """INSERT INTO Passer (ID_commande, courriel) VALUES ({}, "{}");""".format(id_commande, email)
    cursor.execute(request_insert_passer)

# /*
# @Trouver la dernière commande d'un client
# */
def commande_actuelle(email, id_commande):
    request = """SELECT l.isbn, l.titre, l.auteur, l.annee_publication, d.nbr_exemplaire, v.prix FROM Commandes c LEFT JOIN Passer p on c.ID_commande = p.ID_commande LEFT JOIN Contient d on c.ID_commande = d.ID_commande LEFT JOIN Livres l on d.isbn = l.isbn LEFT JOIN Vend v on l.isbn = v.isbn WHERE courriel = "{}" AND c.ID_commande = {}""".format(email, id_commande)
    cursor.execute(request)
    result = cursor.fetchall()
    return result

# /*
# @Ajouter des livres à une commande
# */
def ajout_commande(id_commande, isbn, nbr_exemplaire):
    request = """INSERT INTO Contient (ID_commande, isbn, nbr_exemplaire) VALUES ({}, {}, {});""".format(id_commande, isbn, nbr_exemplaire)
    cursor.execute(request)

# /*
# @Chercher si le livres est dans la DB
# */
def livre_existant(isbn):
    request = """SELECT COUNT(*) FROM Livres WHERE isbn = "{}";""".format(isbn)
    cursor.execute(request)
    fetch = cursor.fetchall()
    result = (fetch[0][0])
    if result > 0:
        return True
    else:
        return False

# /*
# @Vérifie si la quantité voulue est supérieur à la quantité en stock
# */
def quantite_suffisante(isbn, nbr_exemplaire):
    request = """SELECT nbr_exemplaire from Vend WHERE isbn = "{}";""".format(isbn)
    cursor.execute(request)
    fetch = cursor.fetchone()
    result = fetch[0]
    if result >= nbr_exemplaire:
        return True
    else:
        return False

# /*
# @Retourne le coût total d'une commande
# */
def total_cost(id_commande):
    request = "SELECT prix_total from commandes WHERE ID_commande = {}".format(id_commande)
    cursor.execute(request)
    fetch = cursor.fetchone()
    total = fetch[0]
    return total

# /*
# @Payer une commande
# */
def paiement_commande(date_expedition, date_commande, mode_paiement, id_commande):
    request = """UPDATE commandes SET date_expedition = "{}", date_commande = "{}", mode_paiement = "{}" WHERE ID_commande = {};""".format(date_expedition, date_commande, mode_paiement, id_commande)
    cursor.execute(request)

# /*
# @Trouver la dernière commande d'un client
# */
def commande_en_cours(email):
    request = """SELECT * FROM Commandes LEFT JOIN passer on commandes.ID_commande = passer.ID_commande WHERE date_commande is null AND passer.courriel = "{}";""".format(email)
    cursor.execute(request)
    result = cursor.fetchone()
    result_2 = result[0]
    return result_2

# /*
# @Le nombre de commandes par un client avec un vendeur
# */
def commande_par_vendeur(email, ID_vendeur):
    request = """SELECT Vendeurs.ID_vendeur, COUNT(*) FROM Vendeurs JOIN Vend ON Vend.ID_vendeur = Vendeurs.ID_vendeur JOIN Contient on Contient.ISBN = Vend.ISBN JOIN Passer ON Contient.ID_commande = Passer.ID_commande JOIN Clients ON Clients.courriel = Passer.courriel WHERE Clients.courriel = '{}' AND Vendeurs.ID_vendeur = {} GROUP BY Passer.ID_commande, Vendeurs.ID_vendeur""".format(email, ID_vendeur)
    cursor.execute(request)
    result = cursor.fetchall()
    result_nb = result[0][1]
    return result_nb

# /*
# @Le nombre d'évaluation par vendeur
# *
def eval_par_vendeur(email, ID_vendeur):
    request = """SELECT courriel, ID_vendeur, COUNT(*) FROM evalue WHERE courriel = "{}" AND ID_vendeur = {} GROUP BY ID_vendeur, courriel;""".format(email, ID_vendeur)
    cursor.execute(request)
    result = cursor.fetchall()
    if not result:
        return 0
    else:
        result_nb = result[0][2]
        return result_nb

# /*
# @Afficher les lignes de commandes
# *
def ligne_commande(email):
    request = """SELECT Commandes.ID_commande, Livres.titre, vend.prix, Vendeurs.nom, Vendeurs.ID_vendeur, Vendeurs.cote_globale, Commandes.date_commande, Commandes.date_expedition FROM Commandes JOIN Contient on Contient.ID_commande = Commandes.ID_commande JOIN Livres on Contient.isbn = Livres.isbn JOIN Vend ON Livres.isbn = vend.isbn JOIN Vendeurs on Vend.ID_vendeur = Vendeurs.ID_vendeur JOIN Passer on Passer.ID_commande = Commandes.ID_commande WHERE Passer.courriel = '{}'""".format(email)
    cursor.execute(request)
    result = cursor.fetchall()
    return result

# /*
# @Regarde si cela contient un "@"
# *
def is_email(email):
    string = '@'
    if string in email:
        return True
    else:
        return False

# /*
# @Dropbox pour ID_Commande
# */
def insert_review(email, ID_vendeur, cote):
    request = """INSERT INTO Evalue (courriel, ID_vendeur, cote_vendeur) VALUES ("{}",{},{});""".format(email, ID_vendeur, cote)
    cursor.execute(request)

# /*
# @Dropbox pour ID_Commande
# */
def select_id_commande():
    request = """SELECT ID_commande FROM Passer WHERE courriel = "catherinegonzalez@jackson-petersen.org";"""
    cursor.execute(request)
    ids = [entry[0] for entry in cursor.fetchall()]
    return ids

# /*
# @Basé sur le labo
# */
def select_todo_by_id_commande(id_commande):
    request = "SELECT ID_commande FROM Passer WHERE id_commande = {}".format(id_commande)
    cursor.execute(request)
    return cursor.fetchone()[0]