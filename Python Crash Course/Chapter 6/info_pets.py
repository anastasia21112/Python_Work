spot = {
    'Species' : 'Dog',
    'Owner Name' : 'John',
    'Age' : '7'
}

princess = {
    'Species' : 'Dolphin',
    'Owner Name' : 'Sea World',
    'Age' : '5'
}

frog = {
    'Species' : 'Frog',
    'Owner Name' : 'Cecilia',
    'Age' : '1'
}

pets = [spot, princess, frog]

for pet in pets:
    for key, value in pet.items():
        print(f"{key} : {value}")
