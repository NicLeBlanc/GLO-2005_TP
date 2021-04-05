from faker import Faker

fake_data = Faker()

# List of fake company
fake_company = []
for i in range(50):
    fake_company.append(fake_data.company())

# List of fake adress
fake_adress = []
for i in range(50):
    fake_adress.append((fake_data.address()).replace('\n', ', '))

# List of fake e-mail
fake_email = []
for i in range(50):
    fake_email.append(fake_data.email())

# List of fake country
fake_country = []
for i in range(50):
    fake_country.append(fake_data.country())

# List of seller ID
fake_seller_id = []
x = 0
for i in range(50):
    fake_seller_id.append(x + 100000)
    x += 1

# List of seller cote
fake_seller_cote = []
x = 0
for i in range(50):
    fake_seller_cote.append(x)


# List of fake seller
fake_seller = []
fake_list = [fake_seller_id, fake_company, fake_email, fake_adress, fake_country, fake_seller_cote]
for x in range(len(fake_email)):
    fake_seller.append([item[x] for item in fake_list])
print(fake_seller)