# Trent Duncan
# 9/23/24
# pseudocode


# INPUT
base= input("please give the base of the right triangle in ft. ") 
# Convert first piece of input into a number (float)
base = float(base)

height= input("now please insert the height of the right triangle in ft. ")
# Convert second piece of input into a number (float)
height = float(height)


# PROCESS (do something with or to the input)
# Tell Python how to do the math

area = (base * height) / 2

# OUTPUT (Show the answer)

# print(f"A right triangle with a base of {base} feet and a height of {height} feet")
# print(f"has an area of {area} sqaure feet.")

print(f'Right triangle base (ft.): {base}')
print(f'Right triangle height (ft.): {height}')
print(f'Right triangle area (sq. ft.): {area}')


