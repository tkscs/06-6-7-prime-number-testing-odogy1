import random

x = (random.randint(100000000000000000000000000000,999999999999999999999999999999))
z = x/2
if x % 2 != 0:
    z = z + 0.5
z = int(z)
for y in range(100000000000000000000000000000,z):
    if x % y != 0:
        print(x)
    if x % y == 0:
        x = random(100000000000000000000000000000,999999999999999999999999999999)

# This is code to find a 30 diget Prime number.
        
            


