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
	courriel = document.getElementById("courriel").value;
	prenom = document.getElementById("prenom").value;
	nom = document.getElementById("nom").value;
	adresse = document.getElementById("adresse").value;
	date_de_naissance = document.getElementById("date_de_naissance").value;
    var inputClient = {courriel:courriel, prenom:prenom, nom:nom, adresse:adresse, date_de_naissance:date_de_naissance};
    postInscription(inputClient)
}

function postInscription(signupObject) {
    postUrl = "http://127.0.0.1:5000/inscription/"
    fetch(postUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(signupObject)
    }).then(function(response) {
        return response.json()
    }).then(function(data) {
        console.log("worked")
    })
}
