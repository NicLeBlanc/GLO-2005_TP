from database import *
from function import *
import datetime

conn = pymysql.connect(
        host="127.0.0.1",
        user="root123",
        password="123",
        db="livres_en_vrac")

# cmd = 'SELECT * FROM Livres ORDER BY annee_publication DESC limit 10;'
# cur = conn.cursor()
# cur.execute(cmd)
# info = cur.fetchall()
# print(info)

connection = pymysql.connect(
        host="127.0.0.1",
        user="root123",
        password="123",
        db="livres_en_vrac",
        autocommit=True)
cursor = connection.cursor()

# def insert_inscription(courriel, prenom, nom, adresse, date_de_naissance):
#     request = """INSERT INTO Clients (courriel, prenom, nom, adresse, date_de_naissance) VALUES ("{}","{}","{}","{}","{}");""".format(courriel, prenom, nom, adresse, date_de_naissance)
#     cursor.execute(request)
#
# insert_inscription('test','test','test','test','test')

# test = courriel_existant("catherinegonzalez@jackson-petersen.org")
# print(test)
#
# insert_inscription("test","test","test","test","test")
# insert_securise("test","1234")

# print(select_books('titre', 'python'))


# print(set(bonne)-set(mauvaise))
# print(encrypt_pass("test", "test"))

# print(select_books("python"))

# print(courriel_existant("catherinegonzalez@jackson-petersen.org"))

# print("""Livres.{} LIKE "%{}%";""".format('test', 'test'))
#
# create_new_odrder('taylormichael@baker-smith.org')

# def ajout_commande(id_commande, isbn, nbr_exemplaire):
#     request = """INSERT INTO Contient (ID_commande, isbn, nbr_exemplaire) VALUES ({}, {}, {});""".format(id_commande, isbn, nbr_exemplaire)
#     cursor.execute(request)
#
# ajout_commande(2000, 1617291781, 4)
#
# # commande_actuelle()
#
# test = last_order()
# print(test)
#
# print(livre_existant(161729181))
#
# print(quantite_suffisante(1617291781,252))
#
# request = """SELECT nbr_exemplaire from Vend WHERE isbn = 1617291781;"""
# cursor.execute(request)
# fetch = cursor.fetchone()
# result = fetch[0]
# print(result)

# print(commande_actuelle("catherinegonzalez@jackson-petersen.org"))


print(commande_par_vendeur('catherinegonzalez@jackson-petersen.org', 100043))
print(eval_par_vendeur("watkinsheather@yahoo.com", 100029))
print(ligne_commande('catherinegonzalez@jackson-petersen.org'))
