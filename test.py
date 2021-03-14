from faker import Faker
from main import insert_into_clients

fake_data = Faker()

list = [[1,2,3],[4,5,6],[7,8,9]]

liste_vide = []
for x in range(len(list)):
    liste_vide.append([item[x] for item in list])
print(liste_vide)