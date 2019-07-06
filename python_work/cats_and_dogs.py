def print_pet_names(filename):
    try:
        with open(filename) as f_obj:
            lines = f_obj.readlines()
    except FileNotFoundError:
        # print("File " + filename + " not found.")
        pass
    else:
        for line in lines:
            print(line.rstrip())

print_pet_names('cat.txt')
print_pet_names('dogs.txt')
