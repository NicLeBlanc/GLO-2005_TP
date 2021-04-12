from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session, Response
from function import *
from database import *

app = Flask(__name__)
init_Database()
ProfileUtilisateur = {}

conn = connection()

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


@app.route("/inscription/", methods=['GET', 'POST'])
def inscription():
    if request.method == "GET":
        return render_template('inscription.html')

    elif request.method == "POST":
        data = request.json
        courriel = (data["courriel"])
        mot_passe = (data["mot_passe"])
        mot_passe_r = (data["mot_passe_r"])

        if courriel_existant(courriel) is False and mot_passe == mot_passe_r:
            insert_inscription(data["courriel"], data["prenom"], data["nom"], data["adresse"], data["date_de_naissance"])
            insert_securise(data["courriel"], data["mot_passe"])
            insert_prefere(data["courriel"], data["preference"])
            return render_template('inscription.html', message="Votre inscription a fonctionné !")

        elif courriel_existant(data["courriel"]):
            flash("Le courriel existe déjà, veuillez réessayer")
            return render_template('inscription.html', message="Le courriel existe déjà, veuillez réessayer")

        elif data["mot_passe"] != data["mot_passe_r"]:
            flash("Les mots de passe ne correspondent pas, veuillez réessayer")
            return render_template('inscription.html', message="Les mots de passe ne correspondent pas, veuillez réessayer")


@app.route("/inscription_complete", methods=['GET'])
def inscription_complete():
    return render_template('inscription_complete.html')


@app.route("/recherche/", methods=['GET', 'POST'])
def search_books():
    return render_template("recherche2.html")

@app.route("/recherche/resultats_recherche2/", methods=['POST'])
def results():
    recherche = request.form.get('recherche_titre')
    results = select_books(recherche)
    return render_template("results.html", results=results)


# @app.route("/recherche/", methods=['GET', 'POST'])
# def search_books():
#     search_query = request.args.get("query")
#     if search_query is None:
#         return render_template("recherche.html")
#
#     else:
#         books = select_books(search_query)
#
#         response = {
#             "status": 200,
#             "books": books
#         }
#
#         books_json = jsonify(response)
#         return render_template("results.html", books=books_json)
#
#
# @app.route("/recherche/livres/", methods=['GET', 'POST'])
# def display_search():
#     return render_template("results.html")


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run()