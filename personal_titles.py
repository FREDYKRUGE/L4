age = float(input())
sex = input()

if age >= 16:
    if sex == "m":
        print("Mr.")
    if sex == 'f':
        print("Ms.")
else:
    if sex == "m":
        print("Master")
    if sex == 'f':
        print("Miss")