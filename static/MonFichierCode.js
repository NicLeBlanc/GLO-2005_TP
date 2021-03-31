function Fonction1()
{
	document.getElementsByName("ligne1")[0].style.color="red"
	document.getElementsByName("ligne1")[0].innerHTML="Ligne <i>mise &agrave; jour</i> par fonction JavaScript."
}

function Fonction2()
{
	document.getElementsByName("ligne1")[1].style.background="lightgreen"
	document.getElementsByName("ligne1")[1].style.border="10px solid green"
	document.getElementsByName("ligne1")[1].innerHTML="Ligne ind&eacute;pendante."
}

function Fonction3()
{
	document.getElementById("ligne2").style.color="blue";
	document.getElementById("ligne2").innerHTML="Plus de contenu ici!";
	document.getElementById("ligne2").align="right";
}

function SupprimerContenu()
{
	document.getElementsByName("courriel")[0].value="";
	document.getElementsByName("motpasse")[0].value="";
}

function onButtonClickInscription() {
	courriel = document.getElementsByName("courriel");
	prenom = document.getElementsByName("prenom");
	nom = document.getElementsByName("nom");
	adresse = document.getElementsByName("adresse");
	date_de_naissance = document.getElementsByName("date_de_naissance");
    var inputClient = {courriel:courriel, prenom:prenom, nom:nom, adresse:adresse, date_de_naissance:date_de_naissance};
    postInscription(inputClient)
}

function postInscription(courriel, prenom, nom, adresse, date_de_naissance) {
    postUrl = "inscription"

    fetch(postUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            courriel:courriel, prenom:prenom, nom:nom, adresse:adresse, date_de_naissance:date_de_naissance
        })
    }).then(function(response) {
        return response.json()
    }).then(function(data) {
        console.log("worked")
    })
}
