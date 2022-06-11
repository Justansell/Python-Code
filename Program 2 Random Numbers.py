import random
import math
import os

user = os.getlogin()

print(f"Hello {user}, this is my random numbers program!")
#The os module is being used to personalize the program to the user

rand_int = random.randint(1,6)
cube_int = (rand_int**3)

print(f"'{rand_int}' cubed is '{cube_int}'.")

rand_int = random.randint(51,100)
sqrt_int = math.sqrt(rand_int)

print(f"The sqare root of '{rand_int}' is",end=' ')
print(f"'{sqrt_int:.2f}'.")

rand_int = random.randint(10001,30000)

print(f"The digits of '{rand_int}', from ones to ten thousands, are...")

Int1 = rand_int % 10
temp_value = rand_int // 10

Int2 = temp_value % 10
temp_value = temp_value // 10

Int3 = temp_value % 10
temp_value = temp_value // 10

Int4 = temp_value % 10
temp_value = temp_value // 10

Int5 = temp_value % 10

print(Int1,Int2,Int3,Int4,Int5,sep='\n')
