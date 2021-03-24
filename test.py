from faker import Faker
import pymysql.cursors

fake_data = Faker()

list = [[1,2,3],[4,5,6],[7,8,9]]

liste_vide = []
for x in range(len(list)):
    liste_vide.append([item[x] for item in list])
print(liste_vide)

conn = pymysql.connect(
        host="127.0.0.1",
        user="root123",
        password="123",
        db="livres_en_vrac")

cmd = 'SELECT * FROM Livres ORDER BY annee_publication DESC limit 0,10;'
cur = conn.cursor()
cur.execute(cmd)
top10_books = cur.fetchall()
print(top10_books)
