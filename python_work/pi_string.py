# file_path = r"text_files\pi_digits.txt"
file_path = r"text_files\pi_million_digits.txt"
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ""

for line in lines:
    pi_string += line.strip()

# print(pi_string)
# print(pi_string[:52] + "...")
# print(len(pi_string))

birthday = input("Enter your birthday, in the form yymmdd:")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
