filename = 'guests_list'

with open(filename, 'w') as file_object:
    while True:
        name = input("What's your name?\n(Enter 'quit' to quit) ")
        if name == 'quit':
            break
        file_object.write(name + "\n")
