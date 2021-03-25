from flask import Flask, render_template, request
import pymysql, pymysql.cursors

app = Flask(__name__)
ProfileUtilisateur = {}


@app.route("/")
def main():
    return render_template('login.html')


@app.route("/login", methods=['POST'])
def login():
    courriel = '"' + request.form.get('courriel') + '"'
    passe = request.form.get('motpasse')

    conn = pymysql.connect(
        host="127.0.0.1",
        user="root123",
        password="123",
        db="livres_en_vrac")

    cmd = 'SELECT password FROM Clients WHERE courriel=' + courriel + ';'
    cur = conn.cursor()
    cur.execute(cmd)
    passeVrai = cur.fetchone()

    if (passeVrai != None) and (passe == passeVrai[0]):
        cmd = 'SELECT * FROM Clients WHERE courriel=' + courriel + ';'
        cur = conn.cursor()
        cur.execute(cmd)
        info = cur.fetchone()

        global ProfileUtilisateur
        ProfileUtilisateur["courriel"] = info[0]
        ProfileUtilisateur["prenom"] = info[2]
        ProfileUtilisateur["nom"] = info[3]
        return render_template('bienvenu.html', profile=ProfileUtilisateur)

    return render_template('login.html', message="Les informations entrées ne sont pas valides, veuillez ré-essayer")


@app.route("/bienvenu", methods=['POST', 'GET'])
def recent_books():
    conn = pymysql.connect(
        host="127.0.0.1",
        user="root123",
        password="123",
        db="livres_en_vrac")

    cmd = 'SELECT * FROM Livres ORDER BY annee_publication DESC limit 0,2;'
    cur = conn.cursor()
    cur.execute(cmd)
    info = cur.fetchone()

    global livres
    livres["titre"] = info[2]
    livres["auteur"] = info[3]
    # ProfileUtilisateur["nom"] = info[3]

    return render_template('bienvenu.html', livres=livres)


if __name__ == "__main__":
    app.run()
