animals = ["dolphins", "pandas", "owls", "dogs", "peacocks"]
for animal in animals:
	print(f"{animal.title()} are beautiful!")
print("All of these animals are excellent!")

print("The first three items in the list are: ")
for animal in animals[:3]:
	print(animal.title())

print("The middle three items are: ")
for animal in animals[2:5]:
	print(animal.title())

print("The final three items are: ")
for animal in animals[-3:]:
	print(animal.title())
