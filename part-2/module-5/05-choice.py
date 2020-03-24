from random import randint, choice, sample

# with randint it can repeat some numbers, not good for chosen the lottery numbers
for i in range(6):
    print(randint(1, 60), end="-")

print('\n')

# populate a list os numbers to be chosen
lst = []
for i in range(60):
    lst.append(i + 1)

# pickup one number of the list
print(choice(lst))

# pickup 6 numbers from list
print(sample(lst, 6))