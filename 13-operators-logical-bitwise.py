i = 15
j = 22

# If we assume that the integers are stored with 32 bits, the bitwise image of the two variables will be as follows:
# i: 00000000000000000000000000001111
# j: 00000000000000000000000000010110

log = i and j
print(log)


# i 	        00000000000000000000000000001111
# j 	        00000000000000000000000000010110
# bit = i & j 	00000000000000000000000000000110
# 6

bit = i & j
print(bit)


#i 	            00000000000000000000000000001111
# bitneg = ~i 	11111111111111111111111111110000

logneg = not i
print(logneg)

bitneg = ~i
print(bitneg)
