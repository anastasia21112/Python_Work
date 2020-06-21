pizzas = ["pepperoni", "mushroom", "cheese", "margharita"]

friend_pizzas = pizzas[:]

for pizza in pizzas:
	print(f"I like {pizza} pizza")
print("I love pizza!")

pizzas.append("four cheese")
friend_pizzas.append("vegetable")

print(pizzas)
print(friend_pizzas)

print("My favorite pizzas are: ")
for pizza in pizzas: 
	print(pizza)

print("My friend's favorite pizzas are: ")
for friendpizza in friend_pizzas:
	print(friendpizza)
	