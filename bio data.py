name = input("please enter your name:")
birthday = input("please enter your birth date:")
gender = input("please enter your gender:")
phone = input("please enter your phone no:")
email = input("please enter your email id:")
password = input("please enter password:")

a = "profile"
b = "name"
c = "birth date"
d = "gender"
e = "phone no"
g = "email id"
h = "password"

f = open("C:\\Users\\VAMSI\\Desktop\\trainings\\details.txt", "w+")

f.write(f'{a.upper()}' '\n')
f.write(f'{b.upper():<40}{name.upper():<20}''\n')
f.write(f'{c.upper():<40}{birthday.title():<20}''\n')
f.write(f'{d.upper():<40}{gender.upper():<20}''\n')
f.write(f'{e.upper():<40}{phone:<20}''\n')
f.write(f'{g.upper():<40}{email.lower():<20}''\n')
f.write(f'{h.upper():<40}{password:<20}''\n')

f.seek(0)
op = f.read()
print(op)
f.close()