#User Greeting & Birth Year Calculator

name = input("Enter your name: ")
age = int(input("Enter your age: "))

current_year = 2026
birth_year = current_year - age

print(f"Hello {name}! You were likely born in {birth_year}.")