greeley = {
'name' : 'Greeley',
'favorite drink' : 'boba',
'age' : '16',
'sport' : 'track',
'hobby' : 'art'
}

nico = {
'name' : 'Nico',
'favorite drink' : 'sparkling stuff',
'age' : '16',
'sport' : 'pole vault',
'hobby' : 'music'
}

doruk = {
'name' : 'Doruk',
'favorite drink' : 'water',
'age' : '16',
'sport' : 'throwing',
'hobby' : 'paper wall'
}

friends = [greeley, nico, doruk]

for person in friends:
    for key, value in person.items():
        print(f"{key.title()} : {value.title()}")
