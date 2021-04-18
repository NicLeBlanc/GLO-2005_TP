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
SELECT * FROM Vendeurs
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

select * from contient;
select * from clients;

ALTER TABLE contient(ID_commande, isbn, nbr_exemplaire) VALUES (1,"1933988606", 1300);

INSERT INTO contient(ID_commande, isbn, nbr_exemplaire) VALUES (1, "1933988606", 1300);

SELECT distinct b.nbr_exemplaire FROM (contient a, vend b) WHERE (a.isbn = b.isbn)

SELECT * FROM contient c, Vend v WHERE (c.nbr_exemplaire > v.nbr_exemplaire)
SELECT * FROM contient c, Vend v WHERE (c.ID_commande = 1) AND (c.isbn = v.isbn)
SELECT * FROM vendeurs
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
SHOW TABLES
SELECT COUNT(*) FROM Clients WHERE courriel = "catherinegonzalez@jackson-petersen.org";
SELECT * FROM evalue
SELECT *
FROM Livres
ORDER BY annee_publication DESC
limit 0,10;

-- CREATE DATABASE testdb;
-- USE testdb;
-- CREATE TABLE Utilisateurs(courriel varchar(50), motpasse varchar(12), nom varchar(20), avatar varchar(40));
-- INSERT INTO Utilisateurs VALUES("alice@ulaval.ca","12345","Alice", "MonChat.jpg"),("bob@ulaval.ca","qwerty","Bob", "Grimlock.jpg"),("cedric@ulaval.ca","password","C�dric","smiley.gif"),("denise@ulaval.ca","88888888","Denise","reine.jpg");



    request_trigger_changement_commande = """CREATE TRIGGER BeforeInsertCommande
    BEFORE INSERT ON contient
    FOR EACH ROW
    BEGIN
    if (SELECT DISTINCT b.nbr_exemplaire FROM (contient a, vend b) WHERE (a.isbn = b.isbn) AND (a.isbn = NEW.isbn)) < NEW.nbr_exemplaire
    THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Vous tentez de commander plus de livres que ce que le stock peut offrir.';
    END IF;
    END """
    cursor.execute(request_trigger_changement_commande)

    request_trigger_changement_commande_update = """CREATE TRIGGER BeforeUpdateCommande
    BEFORE UPDATE ON contient
    FOR EACH ROW
    BEGIN
    if (SELECT DISTINCT b.nbr_exemplaire FROM (contient a, vend b) WHERE (a.isbn = b.isbn) AND (a.isbn = NEW.isbn)) < NEW.nbr_exemplaire
    THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Vous tentez de commander plus de livres que ce que le stock peut offrir.';
    END IF;
    END """
    cursor.execute(request_trigger_changement_commande_update)


select * from Evalue where courriel = "catherinegonzalez@jackson-petersen.org"
select * from passer where courriel = "catherinegonzalez@jackson-petersen.org"
UPDATE evalue SET ID_Vendeur = 100043 WHERE courriel = "catherinegonzalez@jackson-petersen.org" AND ID_vendeur = 100023;
select * from passer p, commandes where
select * from commandes
select distinct d.nom, d.ID_vendeur, a.ID_commande, e.cote_vendeur
from passer a
     left join contient b on b.ID_commande = a.ID_commande
     left join vend c on c.isbn = b.isbn
     left join vendeurs d on d.ID_vendeur = c.ID_vendeur
     right join evalue e on e.courriel = a.courriel
where a.courriel = "catherinegonzalez@jackson-petersen.org" AND e.ID_vendeur = d.ID_vendeur ;

SELECT ID_commande FROM Passer WHERE courriel = "catherinegonzalez@jackson-petersen.org"
SHOW TABLES
select * from vendeurs

AND e.ID_vendeur = d.ID_vendeur

select distinct f.nom, f.ID_vendeur, c.ID_commande
from passer p, contient c, vend v, vendeurs f
     where p.ID_commande = c.ID_commande
    AND c.isbn = v.isbn
       and v.id_vendeur = f.id_vendeur
AND p.courriel = "catherinegonzalez@jackson-petersen.org";

select distinct f.nom, f.ID_vendeur, c.ID_commande, e.cote_vendeur
from passer p, contient c, vend v, vendeurs f,evalue e
     where p.ID_commande = c.ID_commande
    AND c.isbn = v.isbn
       and v.id_vendeur = f.id_vendeur
AND p.courriel = "catherinegonzalez@jackson-petersen.org"
     AND (e.courriel = p.courriel)
and e.ID_vendeur = f.ID_vendeur;
