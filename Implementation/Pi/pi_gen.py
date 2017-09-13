# http://dept.cs.williams.edu/~heeringa/classes/cs135/s15/readings/spigot.pdf
# https://www.cut-the-knot.org/Curriculum/Algorithms/SpigotForPi.shtml

# Value to determine how many decimal places of Pi to generate
num_digits = 10000

first = [2 for i in range(int((num_digits*10)/3+1))]
first = [x * 10 for x in first]

released = ''
held = []


# Generator
def reverse_index(L):
    for index in reversed(range(len(L))):
        yield index, L[index]


def process_row():
    carryLeft = 0
    for index, item in reverse_index(first):
        if carryLeft != 0:
            item = item + carryLeft
        if index == 0:
            carryLeft = int(item / 10)
            first[index] = item % 10
        else:
            temp = index * 2 + 1
            remainder = item % temp
            quantity = int(item / temp)
            carryLeft = quantity * index
            first[index] = remainder
    return carryLeft


# Do the initial traversal.
value = process_row()
first = [x * 10 for x in first]
released = released + str(value) + '.'

for i in range(num_digits):
    value = process_row()
    first = [x * 10 for x in first]
    if value != 9 and value != 10:
        for number in held:
            released = released + str(number)
        held = [value]
    elif value == 9:
        held.append(value)
    else:
        for j in range(len(held)):
            held[j] = held[j] + 1
            released = released + str(held[j])
        held = [0]
    # print(held)

print(released)
