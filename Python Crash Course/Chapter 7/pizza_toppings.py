message = "Tell me a topping you would like: "
message += "\nEnter 'quit' to stop. "
topping = ''
while topping != 'quit':
    topping = input(message)
    if(topping != 'quit'):
        print(f"{topping.title()} added to pizza")
