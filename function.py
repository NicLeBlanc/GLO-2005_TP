import pymysql
import hashlib
# ***************************************************
# *                 Fonctions                       *
# ***************************************************

connection = pymysql.connect(
        host="127.0.0.1",
        user="root123",
        password="123",
        db="livres_en_vrac",
        autocommit=True)

cursor = connection.cursor()

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
    mot_de_passe_encrypt = encrypt_pass(courriel, mot_de_passe)
    request = """INSERT INTO Securise (courriel, mot_de_passe) VALUES ("{}","{}")""".format(courriel, mot_de_passe_encrypt)
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