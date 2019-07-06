# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't devide by zero!")
print("Give me two numbers, and I'll devide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("First number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't devide by zero!")
    except ValueError:
        print("Please try again.")
    else:
        print(answer)
