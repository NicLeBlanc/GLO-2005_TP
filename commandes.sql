DROP DATABASE IF EXISTS livres_en_vrac;

CREATE DATABASE livres_en_vrac;
USE livres_en_vrac;

CREATE TABLE Clients(courriel varchar(50), password varchar(20), prenom char(20), nom char(20), adresse varchar(200), date_de_naissance nvarchar(50));
SELECT * FROM prefere where courriel = 'test'
SHOW TABLES

SELECT COUNT(*) FROM Clients WHERE courriel = "test";

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

SHOW TRIGGERS
INSERT INTO contient(ID_commande, isbn, nbr_exemplaire) VALUES ("1","193398807X", 10);
SELECT * FROM commandes
SELECT * FROM contient
SELECT DISTINCT ID_commande FROM contient
SELECT * FROM commandes
SELECT * FROM vend WHERE ID_vendeur!=vend.ID_vendeur AND I
SELECT * FROM vend ORDER BY isbn
SELECT * FROM vend
SELECT DISTINCT (isbn) FROM vend
SELECT *, COUNT (DISTINCT (isbn)) FROM vend GROUP BY isbn;
SELECT DISTINCT isbn FROM vend;
SHOW TABLES;
SELECT isbn, COUNT (DISTINCT)

ALTER TABLE contient(ID_commande, isbn, nbr_exemplaire) VALUES (1,"1933988606", 1300);

INSERT INTO contient(ID_commande, isbn, nbr_exemplaire) VALUES (1, "1933988606", 1300);

SELECT distinct b.nbr_exemplaire FROM (contient a, vend b) WHERE (a.isbn = b.isbn)


SELECT * FROM contient c, Vend v WHERE (c.ID_commande = 1) AND (c.isbn = v.isbn)

SELECT * FROM Clients
SELECT * FROM Securise
INSERT INTO contient (ID_commande, isbn, nbr_exemplaire) VALUES ("1","193398807X", 12);
INSERT INTO vendeurs (ID_vendeur, nom, courriel_vendeur, adresse, pays_origine, cote_globale) VALUES(000001, "Tom", "tom@bob.com", "3232323 ddd", "Canada", 0)
SELECT * FROM evalue
SELECT * FROM contient
SELECT * FROM commandes
SELECT * FROM Livres ORDER BY annee_publication DESC limit 10;
SELECT * FROM contient c, Vend v where c.ID_commande = 1 AND c.isbn = v.isbn;
SELECT * FROM contient c, Vend v where c.ID_commande = 1 AND c.isbn = v.isbn;
SELECT * FROM contient
SELECT * FROM vend WHERE isbn = 1933988606
SELECT * FROM vend
request_trigger_Insert_prix_total = """CREATE TRIGGER UpdatePrixTotalInsert AFTER INSERT ON commandes FOR EACH ROW BEGIN
UPDATE commandes SET commandes.prix_total =
(SELECT SUM(c.nbr_exemplaire*v.prix)
FROM Contient c, Vend v WHERE c.ID_commande = new.ID_commande AND c.isbn = v.isbn)
WHERE commandes.ID_commande = new.ID_commmande ;end"""
cursor.execute(request_trigger_Insert_prix_total)

SELECT * FROM contient ORDER BY ID_commande
INSERT INTO contient(contient.ID_commande, isbn, nbr_exemplaire) VALUES (1, "1933988606", 10);
DELETE FROM contient WHERE contient.ID_commande=1 AND isbn = "1933988606";


    request_trigger_Insert_prix_total = """CREATE TRIGGER UpdatePrixTotalInsert AFTER INSERT ON contient FOR EACH ROW BEGIN UPDATE commandes SET commandes.prix_total = (SELECT SUM(c.nbr_exemplaire*v.prix) FROM contient c, Vend v WHERE c.ID_commande = new.ID_commande AND c.isbn = v.isbn) WHERE commandes.ID_commande = new.ID_commmande ;end"""
    cursor.execute(request_trigger_Insert_prix_total)


contient c, Ve
SELECT SUM(c.nbr_exemplaire*v.prix) FROM Contient c, Vend v WHERE c.ID_commande = 1 AND c.isbn = v.isbn;


SELECT * FROM Vend order by ID_vendeur
SELECT DISTINCT isbn FROM Vend
SELECT * FROM livres
SELECT * FROM Clients where courriel = 'test'
SELECT * FROM Securise where courriel = 'test'
SHOW TRIGGERS
SELECT * FROM Evalue


request_trigger_Insert_prix_total = """CREATE TRIGGER UpdatePrixTotalInsert
AFTER INSERT ON contient
FOR EACH ROW
BEGIN
UPDATE commandes SET commandes.prix_total = (100)
WHERE commandes.ID_commande = new.ID_commmande ;end"""
cursor.execute(request_trigger_Insert_prix_total)



request_trigger_Insert_prix_total = """CREATE TRIGGER UpdatePrixTotalInsert
AFTER INSERT ON contient
FOR EACH ROW
BEGIN
UPDATE commandes SET commandes.prix_total = (SELECT SUM(c.nbr_exemplaire*v.prix) FROM Contient c, Vend v WHERE c.ID_commande = new.ID_commande AND c.isbn = v.isbn)
WHERE commandes.ID_commande = new.ID_commmande ;end"""
cursor.execute(request_trigger_Insert_prix_total)


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



