DROP DATABASE IF EXISTS livres_en_vrac;

CREATE DATABASE livres_en_vrac;
USE livres_en_vrac;

CREATE TABLE Clients(courriel varchar(50), password varchar(20), prenom char(20), nom char(20), adresse varchar(200), date_de_naissance nvarchar(50));
SELECT * FROM Clients;

CREATE TABLE Livres(isbn varchar(20), titre varchar(100), auteur char(100), annee_publication int(4), preface varchar(500));

SELECT Password from Securise WHERE courriel = 'aaron11@lucas.com'

SELECT * FROM Livres ORDER BY annee_publication DESC limit 10;

SELECT * FROM Clients where courriel = 'test'

SELECT *
FROM Livres
ORDER BY annee_publication DESC
limit 0,10;

-- CREATE DATABASE testdb;
-- USE testdb;
-- CREATE TABLE Utilisateurs(courriel varchar(50), motpasse varchar(12), nom varchar(20), avatar varchar(40));
-- INSERT INTO Utilisateurs VALUES("alice@ulaval.ca","12345","Alice", "MonChat.jpg"),("bob@ulaval.ca","qwerty","Bob", "Grimlock.jpg"),("cedric@ulaval.ca","password","C�dric","smiley.gif"),("denise@ulaval.ca","88888888","Denise","reine.jpg");