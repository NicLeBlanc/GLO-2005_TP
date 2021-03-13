import pymysql.cursors

connection = pymysql.connect(
    host="127.0.0.1",
    user="root123",
    password="123",
    db="livres_en_vrac",
    autocommit=True
)

def insert_into(text):
    request = """INSERT INTO clients(nom) VALUES ("{}")""".format(text)
    cursor.execute(request)

insert_into("test")
