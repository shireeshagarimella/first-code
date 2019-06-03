j = ['name', 'birth date', 'gender', 'phone no', 'email id', 'password']
k = {}
for l in j:
    i = input("please enter your {} :". format(l))
    k[l] = i

f = open("E:\\Python\\own practice\\bio data.txt", "w+")
f.write(f'{"profile".upper()}' '\n')
for a in k:
    f.write(f'{a.upper():<30}{":":<20}{k[a].upper():<20}''\n')
f.seek(0)
op = f.read()
f.close()
print(op)
