from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session, Response
import datetime
from datetime import date
from function import *
from database import *

app = Flask(__name__)
init_Database()
ProfileUtilisateur = {}

conn = connection()

@app.route("/", methods=['POST', 'GET'])
def main():
    info = select_books_recent()
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
        return render_template('bienvenu.html', profile=ProfileUtilisateur, commandes=getCommandes, recommande=getPreference, pref=getPref)

    return render_template('login.html', message="Les informations entrées ne sont pas valides, veuillez ré-essayer")


@app.route("/bienvenu/", methods=['POST', 'GET'])
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
    courriel = request.form.get('courriel')
    if courriel:
        mot_passe = request.form.get('password')
        mot_passe_r = request.form.get("password_repeat")
        prenom = request.form.get('prenom')
        nom = request.form.get('nom')
        adresse = request.form.get('adresse')
        date_de_naissance = request.form.get('date_de_naissance')
        preference = request.form.get('preference')

        if courriel_existant(courriel) is False and mot_passe == mot_passe_r:
            insert_inscription(courriel, prenom, nom, adresse, date_de_naissance)
            insert_securise(courriel, mot_passe)
            insert_prefere(courriel, preference)
            return render_template('inscription.html', message="Votre inscription a fonctionné !")

        elif is_email(courriel) is False:
            return render_template('inscription.html', message="Le courriel n'est pas valide, il ne contient pas de @")

        elif courriel_existant(courriel):
            return render_template('inscription.html', message="Le courriel existe déjà, veuillez réessayer")

        elif mot_passe != mot_passe_r:
            return render_template('inscription.html', message="Les mots de passe ne correspondent pas, veuillez réessayer")

    return render_template("inscription.html")

# @app.route("/inscription/", methods=['GET', 'POST'])
# def inscription():
#     if request.method == "GET":
#         return render_template('inscription.html')
#
#     elif request.method == "POST":
#         data = request.json
#         courriel = (data["courriel"])
#         mot_passe = (data["mot_passe"])
#         mot_passe_r = (data["mot_passe_r"])
#
#         if courriel_existant(courriel) is False and mot_passe == mot_passe_r:
#             insert_inscription(data["courriel"], data["prenom"], data["nom"], data["adresse"], data["date_de_naissance"])
#             insert_securise(data["courriel"], data["mot_passe"])
#             insert_prefere(data["courriel"], data["preference"])
#             return render_template('inscription.html', message="Votre inscription a fonctionné !")
#
#         elif courriel_existant(data["courriel"]):
#             return render_template('inscription.html', message="Le courriel existe déjà, veuillez réessayer")
#
#         elif data["mot_passe"] != data["mot_passe_r"]:
#             return render_template('inscription.html', message="Les mots de passe ne correspondent pas, veuillez réessayer")


@app.route("/recherche/", methods=['GET', 'POST'])
def search_books():
    return render_template('recherche.html')


@app.route("/recherche/resultats_recherche/", methods=['POST','GET'])
def results():
    recherche = request.form.get('recherche_titre')
    type_recherche = request.form.get('type_recherche')
    results = select_books(type_recherche, recherche)
    return render_template('results.html', results=results, recherche=recherche, type_recherche=type_recherche)


@app.route("/commande/", methods=['GET', 'POST'])
def recent_commande():
    result = get_commandeCourante(ProfileUtilisateur["courriel"])
    contenu = get_commandeContenu(ProfileUtilisateur["courriel"])
    return render_template('commande.html', result=result, contenu=contenu, profile=ProfileUtilisateur)


@app.route("/nouvelle_commande", methods=['GET', 'POST'])
def nouvelle_commande():
    ajouter_commande = request.form.get('ajout_commande')
    last_order_num = int(last_order()) - 1
    if not ajouter_commande:
        new_order = last_order()
        create_new_odrder(ProfileUtilisateur["courriel"], new_order)
    else:
        nbr_exemplaire = int(request.form.get('nbr_exemplaire'))
        if livre_existant(ajouter_commande):
            if quantite_suffisante(ajouter_commande, nbr_exemplaire):
                livre_isbn = int(request.form.get('ajout_commande'))
                ajout_commande(last_order_num, livre_isbn, nbr_exemplaire)
            else:
                message = '''La quantité commandée est supérieur à celle disponible'''
                return render_template('nouvelle_commande.html', message=message)
        else:
            message='''Le livre n'existe pas'''
            return render_template('nouvelle_commande.html', message=message)

    commande = commande_actuelle(ProfileUtilisateur["courriel"], last_order_num)
    cout_total = total_cost(last_order_num)
    return render_template('nouvelle_commande.html', commande=commande, cout_total=cout_total)


@app.route("/payer_commande", methods=['GET', 'POST'])
def payer_commande():
    mode_paiement = request.form.get('mode_paiement')
    if mode_paiement:
        today = date.today()
        date_commande = today.strftime('%Y-%m-%d')
        time_change = datetime.timedelta(days=7)
        date_exp = today + time_change
        date_expedition = date_exp.strftime('%Y-%m-%d')
        id_commande_cours = commande_en_cours(ProfileUtilisateur["courriel"])
        prenom = ProfileUtilisateur["prenom"]
        nom = ProfileUtilisateur["nom"]
        cout_total = total_cost(id_commande_cours)
        paiement_commande(date_expedition, date_commande, mode_paiement, id_commande_cours)
        return render_template('paiement_complet.html', date_commande = date_commande, date_expedition=date_expedition, mode_paiement=mode_paiement, montant_total=cout_total, nom=nom, prenom=prenom)

    return render_template('paiement.html')

@app.route("/evaluation", methods=['GET', 'POST'])
def evaluation():
    commandes = ligne_commande(ProfileUtilisateur["courriel"])
    id_vendeur = request.form.get('ID_vendeur')
    if id_vendeur:
        cote = request.form.get('cote')
        commande_vendeur = commande_par_vendeur(ProfileUtilisateur["courriel"],id_vendeur)
        eval_vendeur = eval_par_vendeur(ProfileUtilisateur["courriel"],id_vendeur)
        if commande_vendeur > eval_vendeur:
            insert_review(ProfileUtilisateur["courriel"],id_vendeur,cote)
            message = "Merci pour votre évaluation !"
            return render_template('evaluation_vendeur.html', commandes=commandes, message=message)
        else:
            message = "Vous avez déjà évalué ce vendeur"
            return render_template('evaluation_vendeur.html', commandes=commandes, message=message)
    return render_template('evaluation_vendeur.html', commandes=commandes)

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run()