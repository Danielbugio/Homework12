import random

countries_cities = {"Austria": "Vienna", "Croatia": "Zagreb", "Spain": "Madrid", "Portugal": "Lisboa", "Italia": "Roma", "Venezuela": "Peru"}
countrie_city_rand = random.choice(list(countries_cities.items()))



name = input("What's your name: ")
print ("What is the capital of " + str(countrie_city_rand[0]) + "?")

city = input()

if city == countrie_city_rand[1]:
    print ("You're correct")
else:
    print("You're wrong")
