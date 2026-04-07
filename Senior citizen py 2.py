name = input("Enter name: ")
birth_year = int(input("Enter year of birth: "))

current_year = 2026
age = current_year - birth_year

if age >= 60:
    print(name, "is a Senior Citizen")
else:
    print(name, "is not a Senior Citizen")