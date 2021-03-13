import pymysql.cursors

connection = pymysql.connect(
    host="127.0.0.1",
    user="root123",
    password="123",
    db="livres_en_vrac",
    autocommit=True
)

cursor = connection.cursor()

def insert_into_clients(colone, text):
     request = """INSERT INTO Clients({}) VALUES ("{}")""".format(colone, text)
     cursor.execute(request)
