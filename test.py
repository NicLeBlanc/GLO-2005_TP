from database import *
from function import *

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

print(courriel_existant("catherinegonzalez@jackson-petersen.org"))

print("""Livres.{} LIKE "%{}%";""".format('test', 'test'))