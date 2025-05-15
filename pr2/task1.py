class Student:
    def __init__(self,surname,birthday,numgroup,progress):
        self.surname = surname
        self.birthday = birthday
        self.numgroup = numgroup
        self.progress = progress

    def change_surname(self, new_surname):
        self.surname = new_surname
    def change_birthday(self, new_birthday):
        self.birthday = new_birthday
    def change_numgroup(self, new_numgroup):
        self.numgroup = new_numgroup

    def output_info(self):
        conclusion = (f"Фамилия: {self.surname}\tДата рождения: {self.birthday}\n"
                      f"Номер группы: {self.numgroup}\tУспеваемость: {self.progress}")
        print(conclusion)

student1 = Student("Котов", "04.04.2004", "632", [5, 4, 3, 5, 4])
student2 = Student("Кошечкина", "03.03.2003", "631", [4, 5, 4, 4, 3])

student1.change_numgroup("432")
student1.output_info()
student2.output_info()