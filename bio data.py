name = input("please enter your NAME:")
birthday = input("please enter your BIRTH date:")
gender = input("please enter your GENDER:")
password = input("please enter PASSWORD:")

e="PROFILE"
a="NAME"
b="Birthdate"
c="Gender"
d="PASSWORD"

f = open("C:\\Users\\VAMSI\\Desktop\\trainings\\details.docx", "w+")

f.write(f'{e}' '\n')
f.write(f'{a:<40}{name.upper():<20}''\n')
f.write(f'{b:<40}{birthday.title():<20}''\n')
f.write(f'{c:<40}{gender.upper():<20}''\n')
f.write(f'{d:<40}{password:<20}''\n')

f.seek(0)
op=f.read()
print(op)
f.close()