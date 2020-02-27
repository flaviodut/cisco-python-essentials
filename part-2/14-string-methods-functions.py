name = 'Flavio Alberto Dutra'

print('vio' in name)
print('d' in name)
print('xyz' not in name)

print('(' + min(name) + ')')
print('(' + max(name) + ')')

# position
print(name.index('A'))

# to array
print(list(name))

# counter
print(name.count('l'))

# capitalize
print('flávio'.capitalize())

# upper / center / lower / swapcase / title
print('flávio'.upper().center(20, '*'))

# endswitch / startswith
print(name.endswith('utra'))
print(name.startswith('utra'))

# find (saffer then index 'cause it returns -1 if didnt find anything
# rfind (right)
print(name.find('utra'))

# contains number characters?
print('lambda30'.isalnum())

# letters only?
print('lambda30'.isalpha())

# digits only?
print('lambda30'.isdigit())

# islower()
# isspace()
# issupper()

# join / split
print('.'.join(['1', '2', '3']))
print(name.split())

# lstrip / rstrip / trip
print('   name name      '.lstrip().rstrip())
print('   name name      '.strip())
print('www.cisco.com'.lstrip('w.'))
print('www.cisco.com'.rstrip('com'))

# replace
print("iiiiiiiii".replace("i", "W"))
print("iiiiiiiii".replace("i", "W", 1))
print("iiiiiiiii".replace("i", "W", 3))