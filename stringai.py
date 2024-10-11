# print("1. STRINGS užd. - atspausdinti trumpesnį variantą")
# vardas = "Tim"
# pavarde = "Robbins"
#
# if len(vardas) < len(pavarde):
#     print(vardas)
# elif len(pavarde) < len(vardas):
#     print(pavarde)
# else:
#     print("Vardas ir pavarde tai lygaus ilgio!")
from curses.ascii import isdigit

# print("2. STRINGS užd. - UPPER lower")
# vardas = "Tim"
# pavarde = "Robbins"
# print(vardas.upper())
# print(pavarde.lower())

# print("3. STRINGS užd. - pirmos raides")
# vardas = "Tim"
# pavarde = "Robbins"
# trecias = vardas[0]+pavarde[0]
# print(trecias)

# print("4. STRINGS užd. - pirmos raides")
# vardas = "Tim"
# pavarde = "Robbins"
# trecias = vardas[-3:]+pavarde[-3:] # gal geriau uzsaugot 3 kaip kintamaji?..
# print(trecias)

# print("5. STRINGS užd. - pakeist a i zvaigzdute")
# string = "An American in Paris"
# string2 = string.replace("a", "*")
# string3 = string2.replace("A", "*")
# print(string3)

# print("6. STRINGS užd. - istrinti balses")
# string1 = "An American in Paris"
# string2 = "Breakfast at Tiffany's"
# string3 = "2001: A Space Odyssey"
# string4 = "It's a Wonderful Life"
#
# balses = ("a", "e", "i", "o", "u")
# balses2 = ['a', 'e', 'i', 'o', 'u']
# balses3 = ['AEIOUaeiou']
# # print(string1.replace('[AEIOUaeiou]', ""))
# print(string1.strip(balses3))

print("7. STRINGS užd. - surasti epizodo numeri")
import random
starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
print(starWars)

x = starWars.find("[1234567890]")
print(starWars[x])

y = starWars.rfind("1234567890")
print(starWars[y])

z = starWars.index("1234567890")
print(starWars[z])

u = starWars.index("[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]")
print(starWars[u])

w = starWars.index("1, 2, 3, 4, 5, 6, 7, 8, 9, 0")
print(starWars[w])




