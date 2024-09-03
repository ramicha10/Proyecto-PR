a = "emiliano"
b = a
c = a + b
a = 124
print(a)
print(b)
print(c)
if a == 123:
    a = "hola"
    # c = a + b
    print(c)
else:
    if a == 124:
        print("a es igual a 124")
    print("a no es igual a 123")

print(a)
for i in range(10):
    d = 1
    print(i)
    a = a + i
    print(a)
#c = a + b
#print(c)
print(a)
print(d + a)
