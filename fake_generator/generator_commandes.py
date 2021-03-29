import random
from faker import Faker
import datetime

#(ID_commande, niveau_satisfaction, prix_total, date_expedition, date_commande)

ID_commande = []
id = 1
for i in range(1000):
    ID_commande.append(id)
    id += 1
print(ID_commande)

niveau_satisfaction = []
for i in range(1000):
    niveau_satisfaction.append(random.randint(1,5))
print(niveau_satisfaction)

fake_data = Faker()
date_commande = []
datetime_commande = []
for i in range(1000):
    date = (fake_data.date_between('-2y','today'))
    datetime_commande.append(date)
    date_commande.append(date.strftime('%Y-%m-%d'))
print(date_commande)

ship_time = []
for i in datetime_commande:
    time_change = datetime.timedelta(days=7)
    date = (i + time_change)
    ship_time.append(date.strftime('%Y-%m-%d'))
print(ship_time)
