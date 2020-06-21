guestList = ["Greeley", "Nico", "Doruk"]
print(f"Hey {guestList[0]}, can you come to dinner")
print(f"Hey {guestList[1]}, can you come to dinner")
print(f"Hey {guestList[2]}, can you come to dinner")

print(f"Oh no! {guestList[0]} can't come!")

print(f"{len(guestList)} are coming to dinner!")

guestList[0] = 'Seth'
print(f"Hey {guestList[0]}, can you come to dinner?")
print(f"Hey {guestList[1]}, can you come to dinner?")
print(f"Hey {guestList[2]}, can you come to dinner?")

print("I FOUND A WAY BIGGER TABLE!")

guestList.insert(2, "Evan")
guestList.insert(0, "Emily")
guestList.append("Daphne")

print(f"Hey {guestList[0]}, can you come to dinner?")
print(f"Hey {guestList[1]}, can you come to dinner?")
print(f"Hey {guestList[2]}, can you come to dinner?")
print(f"Hey {guestList[3]}, can you come to dinner?")
print(f"Hey {guestList[4]}, can you come to dinner?")
print(f"Hey {guestList[5]}, can you come to dinner?")

print("Ugh, actually we only have room for two people!")

uninvitedGuest = guestList.pop()
print(f"I'm sorry {uninvitedGuest}, you can't come")

uninvitedGuest = guestList.pop()
print(f"I'm sorry {uninvitedGuest}, you can't come")

uninvitedGuest = guestList.pop()
print(f"I'm sorry {uninvitedGuest}, you can't come")

uninvitedGuest = guestList.pop()
print(f"I'm sorry {uninvitedGuest}, you can't come")

print(f"Hey! You're still invited {guestList[0]}")
print(f"Hey! You're still invited {guestList[1]}")

del guestList[0]
del guestList[0]

print(guestList)

print(f"{len(guestList)} are coming!")


