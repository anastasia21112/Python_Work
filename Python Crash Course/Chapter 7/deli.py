sandwich_orders = ['tuna', 'meatball', 'taco', 'fish', 'pastrami', 'noodle', 'egg salad', 'pastrami', 'roast beef', 'pastrami']

finished_sandwiches = []

print("Oh no, the deli is out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    new_finished_sandwiches = sandwich_orders.pop();

    print(f"{new_finished_sandwiches.title()} sandwich is made!")
    finished_sandwiches.append(new_finished_sandwiches)
