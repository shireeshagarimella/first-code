f = open("E:\\Python\\own practice\\details1.txt","r")
x = f.read()
f.close()
s = x.split('\n')
k = []
for l in s:
    i = input(l)
    k.append(i)
y = ':'
j = ['name', 'birth date', 'gender', 'phone no', 'email id', 'password']
f = open("E:\\Python\\own practice\\bio data.txt", "w+")
f.write(f'{"profile".upper()}' '\n')
for a, b in zip(k, j):
    f.write(f'{b.upper():<20}{y:<20}{a.upper():<20}''\n')
f.seek(0)
op = f.read()
f.close()
print(op)
