f1 = open("C:\\Users\\VAMSI\\Desktop\\trainings\\duplicate files.txt", 'w+')
f1.write("Python learning course has \n""strings \n""lists \n""tuples \n""dictionaries \n""files \n""strings \n")
f1.write("Python learning course has \n""strings \n""lists \n""tuples \n""dictionaries \n""files \n""strings \n")
f1.write("Python learning course has \n""strings \n""lists \n""tuples \n""dictionaries \n""files \n""strings \n")
f1.seek(0)
str = f1.read()
f1.close()
print("***********")
print(str)
str1 = str.split('\n')
str2 = "\n".join(sorted(set(str1), key=str1.index))
print("************")
print(str2)
print("***********")
f2 = open("C:\\Users\\VAMSI\\Desktop\\trainings\\duplicate deleted files.txt", 'w+')
f2.write(str2)
f2.seek(0)
c = f2.read()
print(c)
f2.close()


