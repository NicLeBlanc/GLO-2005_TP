import pymysql as pymysql
from flask import Flask, render_template, request, jsonify, redirect, url_for
from function import *
from database import *

app = Flask(__name__)
init_Database()
ProfileUtilisateur = {}

conn = pymysql.connect(
        host="127.0.0.1",
        user="root123",
        password="123",
        db="livres_en_vrac")

@app.route("/", methods=['POST', 'GET'])
def main():
    cmd = 'SELECT * FROM Livres ORDER BY annee_publication DESC limit 10;'
    cur = conn.cursor()
    cur.execute(cmd)
    info = cur.fetchall()
    return render_template('login.html', livres=info)

@app.route("/login", methods=['POST'])
def login():
    courriel = '"' + request.form.get('courriel') + '"'
    passe = request.form.get('motpasse')

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

        getCommandes = get_commandes(ProfileUtilisateur["courriel"])
        getPreference = get_preferences(ProfileUtilisateur["courriel"])
        getPref = get_pref(ProfileUtilisateur["courriel"])
        return render_template('bienvenu.html', profile=ProfileUtilisateur, commandes=getCommandes, recommande = getPreference, pref = getPref)

    return render_template('login.html', message="Les informations entrées ne sont pas valides, veuillez ré-essayer")


@app.route("/bienvenu", methods=['POST', 'GET'])
def recent_books():
    pass

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

        if courriel_existant(data["courriel"]) is True:
            return render_template("inscription.html", message = "Ce courriel est déjà utilisé, veuillez recommencer")

        if data["mot_passe"] != data["mot_passe_r"]:
            return render_template("inscription.html", message = "Les deux mots de passe entrés ne sont pas identiques, veuillez recommencer")

        else:
            insert_inscription(data["courriel"], data["prenom"], data["nom"], data["adresse"], data["date_de_naissance"])
            insert_securise(data["courriel"], data["mot_passe"])
            return render_template('inscription_complete.html')
    else:
        return render_template('inscription.html')


@app.route("/inscription_complete", methods=['POST', 'GET'])
def inscription_complete():
    return render_template('inscription_complete.html')


@app.route("/recherche", methods=['POST', 'GET'])
def search_books():
    return render_template('recherche.html')




if __name__ == "__main__":
    app.run()