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
import random
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



# print("4. STRINGS užd. - trys paskutines raides")
# vardas = "Tim"
# pavarde = "Robbins"
# trecias = vardas[-3:] + pavarde[-3:] # gal geriau uzsaugot 3 kaip kintamaji?..
# print(trecias)



# print("5. STRINGS užd. - pakeist a i zvaigzdute")
# string = "An American in Paris"
# string2 = string.replace("a", "*")
# string3 = string2.replace("A", "*")
# print(string3)



# #### --- SPRENDIMAS 6 --- ####
# print("6. STRINGS užd. - istrinti balses")
# filmas1 = "An American in Paris"
# filmas2 = "Breakfast at Tiffany's"
# filmas3 = "2001: A Space Odyssey"
# filmas4 = "It's a Wonderful Life"
# print(filmas1)
#
# filmas = filmas3
# x = filmas.replace('A', "")
# x2 = x.replace('i', "")
# x3 = x2.replace('e', "")
# x4 = x3.replace('u', "")
# x5 = x4.replace('o', "")
# x6 = x5.replace('a', "")
# x7 = x6.replace('O', "")
# print(x7)
# #### --- SPRENDIMAS 6 --- ####







# balses = ("a", "e", "i", "o", "u")
# balses2 = ['a', 'e', 'i', 'o', 'u']
# balses3 = ['AEIOUaeiou']
# balses4 = "a", "e", "i", "o", "u"
# vowels = {'i','o','a','u','e'}
# string1.strip(vowels)
# import re
# re.sub('[aeiou]', '', string1)

## --- SPRENDIMAS 7 --- ###
# print("7. STRINGS užd. - surasti epizodo numeri")
# import random
# starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
# print(starWars)
#
# import re
# numbers = re.findall('\d', starWars)
# print(numbers)
## --- SPRENDIMAS 7 --- ###




###### --- BANDYMAI --- #####
# numbers = [123456789]
# numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
# x = starWars.isdigit()
# x = starWars.find('123456789')
# print(x)

# y = starWars.rfind("1234567890")
# print(starWars[y])
#
# z = starWars.index("1234567890")
# print(starWars[z])
#
# u = starWars.index("[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]")
# print(starWars[u])
#
# w = starWars.index("1, 2, 3, 4, 5, 6, 7, 8, 9, 0")
# print(starWars[w])




## --- PAPILDOMAI --- ###
# ## --- SPRENDIMAS 8 --- ###
# print("8. STRINGS užd. - trumpiau ilgiau nei 5 raides")
# stringas = "Don't Be a Menace to South Central While Drinking Your Juice in the Hood"
# stringas2 = "Tik nereikia gąsdinti Pietų Centro, geriant sultis pas save kvartale kvartale"
# x = stringas2.split()
# print(x)
# print(len(x)) # zodziu kiekis
#
# ilgesni_zodziai = 0
# # tie_zodziai = []
# for word in x:
#     if len(word) >= 5:
#         ilgesni_zodziai += 1
# #        tie_zodziai += word
# print(f'Tiek turim zodziu is 5 ar daugiau raidziu: {ilgesni_zodziai}')
# ## --- SPRENDIMAS 8 --- ###



# print(stringas)
# zodziu_kiekis = 1
# for i in stringas:
#     if i == " ":
#         tarpai += 1
# print(zodziu_kiekis)


### --- 9 uzduotis - 3 random lotyniskos raides --- ###
# import random
# atsitiktinis_stringas = ''
# alpha = 'abcdefghijklmnopqrstuvwxyz'
# for i in range(0,3):
#     atsitiktinis_stringas += random.choice(alpha)
# print(atsitiktinis_stringas)




### --- 10 uzduotis - 10 random zodziu is 8 uzd --- ###
stringas = "Don't Be a Menace to South Central While Drinking Your Juice in the Hood"
stringas2 = "Tik nereikia gąsdinti Pietų Centro, geriant sultis pas save kvartale kvartale"
x = stringas.split()
print(x)
x2 = stringas2.split()
print(x2)
x3 = x + x2

import random
atsitiktinis_stringas = []
for i in range(0,10):
    if i not in atsitiktinis_stringas:
      atsitiktinis_stringas.append(random.choice(x3))
print(atsitiktinis_stringas)
