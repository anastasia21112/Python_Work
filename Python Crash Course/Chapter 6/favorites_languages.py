languages = {'Lam' : 'Python',
            'Bobby' : 'Python',
            'Ross' : 'Java',
            'Dillon' : 'Java',
            'Anastasia' : 'Go',
            'Harrison' : 'Python',
            'Jonah' : 'JavaScript',
            'Topher' : 'Swift'
            }
people = ['Greeley', 'Nico', 'Sophie', 'Myles', 'Lam', 'Fifi', 'Bobby', 'Harrison']

for name in people:
    if name not in languages.keys():
        print(f"{name} should take the poll")
    else:
        print(f"{name}, thank you for responding")
