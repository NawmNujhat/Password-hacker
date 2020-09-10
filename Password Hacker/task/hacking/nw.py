import string
symbols=string.ascii_letters+string.digits
characters = [c for c in string.ascii_letters] + [str(n) for n in range(10)]
print(characters)
print(symbols)
password=""
for char in symbols:
    password+=char
print(password)