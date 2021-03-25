import pymysql.cursors

conn = pymysql.connect(
        host="127.0.0.1",
        user="root123",
        password="123",
        db="livres_en_vrac")

cmd = 'SELECT * FROM Livres ORDER BY annee_publication DESC limit 10;'
cur = conn.cursor()
cur.execute(cmd)
info = cur.fetchall()
print(info)
