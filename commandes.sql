DROP DATABASE IF EXISTS livres_en_vrac;

CREATE DATABASE livres_en_vrac;
USE livres_en_vrac;

CREATE TABLE Clients(courriel varchar(50), password varchar(20), prenom char(20), nom char(20), adresse varchar(200), date_de_naissance nvarchar(50));
SELECT * FROM Clients;
SHOW TABLES

SHOW INDEXES FROM Livres
SHOW INDEXES FROM Securise
CREATE TABLE Livres(isbn varchar(20), titre varchar(100), auteur char(100), annee_publication int(4), preface varchar(500));

SELECT * from Securise WHERE courriel = 'aaron11@lucas.com'
SELECT * FROM passer

#Analyse de temps d'opération
EXPLAIN ANALYZE SELECT * FROM Livres ORDER BY annee_publication DESC limit 10;
ALTER TABLE Livres DROP INDEX btree_livres

#Analyse des triggers
SHOW TRIGGERS
INSERT INTO Evalue(courriel, ID_vendeur, cote_vendeur) VALUES ("aaron11@lucas.com","100001",5);
SELECT * FROM vendeurs
SELECT * FROM Evalue ORDER BY ID_vendeur

#Analyse trigger commande





SELECT * FROM Clients

INSERT INTO vendeurs (ID_vendeur, nom, courriel_vendeur, adresse, pays_origine, cote_globale) VALUES(000001, "Tom", "tom@bob.com", "3232323 ddd", "Canada", 0)


SELECT * FROM Livres ORDER BY annee_publication DESC limit 10;
SELECT * FROM contient
SELECT * FROM Vend
SELECT * FROM livres
SELECT * FROM Clients where courriel = 'test'
SELECT * FROM Securise where courriel = 'test'
SHOW TRIGGERS
SELECT * FROM Evalue

SELECT * FROM Commandes join Passer on Commandes.ID_commande = Passer.ID_commande WHERE courriel = 'aaron84@yahoo.com'
SHOW TRIGGERS
SHOW INDEXES
SELECT * FROM Vendeurs

SELECT type FROM prefere WHERE courriel = 'aaron84@yahoo.com'

SELECT COUNT(*) FROM Clients WHERE courriel = "catherinegonzalez@jackson-petersen.org";

SELECT *
FROM Livres
ORDER BY annee_publication DESC
limit 0,10;

-- CREATE DATABASE testdb;
-- USE testdb;
-- CREATE TABLE Utilisateurs(courriel varchar(50), motpasse varchar(12), nom varchar(20), avatar varchar(40));
-- INSERT INTO Utilisateurs VALUES("alice@ulaval.ca","12345","Alice", "MonChat.jpg"),("bob@ulaval.ca","qwerty","Bob", "Grimlock.jpg"),("cedric@ulaval.ca","password","C�dric","smiley.gif"),("denise@ulaval.ca","88888888","Denise","reine.jpg");



