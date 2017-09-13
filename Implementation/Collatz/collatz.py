value = input("Please enter a number...\n")
try:
    value = int(value)
except ValueError:
    print("\nYou did not enter a valid integer...")

counter = 0

while value != 1:
    if value % 2 == 0:
        value = value / 2
    else:
        value = value * 3 + 1
    print(value)
    counter = counter + 1

print("The number of steps to reach 1 is", counter)