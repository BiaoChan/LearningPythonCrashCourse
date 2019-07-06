filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

words = contents.split()
print(len(words))


print(contents.count('and'))
print(contents.lower().count('and'))
