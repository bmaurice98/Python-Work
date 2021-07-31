import sys
import getopt

# Print Hello world
print("Hello world\n")
hello = "Hello"
world = "World"
print(hello, world, world, hello, "\n")
hWorld = ["hello", "world"]
print(hWorld)
print(hWorld[0])

# Return types
print(type("def"))
print(type(b"def"))
print(type("D"))
print(type(3))
print(type(3.3))

# Return range() of number
for x in range(1, 5):
    print(x)

# Error Handling
try:
    trying_to_catch_error

except NameError as err:
    print(err, "error caused")

# Arithmetic
print(4 + 3)
print(29 / 3)

# Translate binary > string
binary = "10101110"

ascii_character = int(binary, 2)

print(chr(ascii_character))
