first = int(input("Give me the first number: "))
second = int(input("Give me the second number: "))
print("Thank you!")
print(f"{first} + {second} = {first + second}")
print(f"{first} - {second} = {first - second}")
if second != 0:
    print(f"{first} / {second} = {(first / second):.0f}")
print(f"{first} * {second} = {first * second}")