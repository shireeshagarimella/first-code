class Student():
    def name(self):
        x = input("Enter your name")
        self.yname = x

    def details(self):
        print("your name is : ", self.yname)


stu = Student()
stu.name()
stu.details()
print(dir(stu))
