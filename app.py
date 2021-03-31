import pymysql.cursors
from flask import Flask, render_template, request, jsonify
from database import *

app = Flask(__name__)
ProfileUtilisateur = {}
init_Database()

@app.route("/", methods=['POST', 'GET'])
def main():

    conn = pymysql.connect(
        host="127.0.0.1",
        user="root123",
        password="123",
        db="livres_en_vrac")

    cmd = 'SELECT * FROM Livres ORDER BY annee_publication DESC limit 10;'
    cur = conn.cursor()
    cur.execute(cmd)
    info = cur.fetchall()
    return render_template('login.html', livres=info)

@app.route("/login", methods=['POST'])
def login():
    courriel = '"' + request.form.get('courriel') + '"'
    passe = request.form.get('motpasse')

    conn = pymysql.connect(
        host="127.0.0.1",
        user="root123",
        password="123",
        db="livres_en_vrac")

    cmd = 'SELECT mot_de_passe FROM Securise WHERE courriel=' + courriel + ';'
    cur = conn.cursor()
    cur.execute(cmd)
    passeVrai = cur.fetchone()
    crypted_pass = encrypt_pass(courriel, passe)

    if (passeVrai != None) and (crypted_pass == passeVrai[0]):
        cmd = 'SELECT * FROM Clients WHERE courriel =' + courriel + ';'
        cur = conn.cursor()
        cur.execute(cmd)
        info = cur.fetchone()

        global ProfileUtilisateur
        ProfileUtilisateur["courriel"] = info[0]
        ProfileUtilisateur["prenom"] = info[1]
        ProfileUtilisateur["nom"] = info[2]

        return render_template('bienvenu.html', profile=ProfileUtilisateur)

    return render_template('login.html', message="Les informations entrées ne sont pas valides, veuillez ré-essayer")


@app.route("/bienvenu", methods=['POST', 'GET'])
def recent_books():
    conn = pymysql.connect(
        host="127.0.0.1",
        user="root123",
        password="123",
        db="livres_en_vrac")

    # cmd = 'SELECT * FROM Livres ORDER BY annee_publication DESC limit 1;'
    # cur = conn.cursor()
    # cur.execute(cmd)
    # info = cur.fetchone()
    #
    # return render_template('bienvenu.html', livres=info)


@app.route("/inscription/", methods=['GET','POST'])
def inscription():
    if request.method == "GET":
        pass
    if request.method == "POST":
        data = request.json
        insert_inscription(data["courriel"], data["prenom"], data["nom"], data["adresse"], data["date_de_naissance"])
        return render_template('inscription_complete.html')
    else:
        return render_template('inscription.html')

# @app.route("/inscription_complete", methods=['POST', 'GET'])
# def inscription():
#     courriel = '"' + request.form.get('courriel') + '"'
#     return render_template("inscription_complete.html")

    # return render_template('inscription.html', message="Cette adresse courriel est d&eacutej&agrave utilis&eacutee ou des information entr&eacutees ne sont pas conformes")

if __name__ == "__main__":
    app.run()