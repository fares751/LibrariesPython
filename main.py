from dadjokes import Dadjoke
from faker import Faker

print("1. Dadjokes")

dad_joke = Dadjoke()
joke = dad_joke.joke
print(joke)

print("\n2. Faker")

fake = Faker("de_DE")
name = fake.name()
address = fake.address()

print(name)
print(address)

print("\n3. Dadjokes und Faker kombinieren")

# Die Adresse für den Satz in eine Zeile bringen
address_one_line = address.replace("\n", ", ")

print(f"{name} wohnt hier: {address_one_line}.")
print(f"Der Lieblingswitz von {name} lautet: „{joke}“")