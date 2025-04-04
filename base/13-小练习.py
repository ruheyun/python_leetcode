class Student:
    def __init__(self, name, age, gender, score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def info(self):
        print(f'姓名：{self.name}, 年龄：{self.age}, 性别：{self.gender}, 分数：{self.score}')

lst = []
for i in range(5):
    info = input('请输入个人信息：')
    str = info.split('#')
    stu = Student(str[0], str[1], str[2], str[3])
    lst.append(stu)

for i in range(5):
    lst[i].info()