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
# @Affichage des 10 livres les plus récents
# */

def select_books_recent():
    request = "SELECT * FROM Livres ORDER BY annee_publication DESC LIMIT 0,10;"
    cursor.execute(request)
    books = [entry[0] for entry in cursor.fetchall()]
    return books

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
def select_books(query=None):
    request = "SELECT * from Livres"
    if request:
        request += """ WHERE titre LIKE '%{}%'""".format(query)
    request += ';'
    cursor.execute(request)
    books = cursor.fetchall()
    return books

