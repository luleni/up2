class Worker:
    def __init__(self,name,surname,rate,days):
        self.name = name
        self.surname = surname
        self.rate = int(rate)
        self.days = int(days)
    def GetSalary(self):
        salary = self.rate * self.days
        return salary
    def output_info(self):
        print('Имя:',self.name)
        print('Фамилия:', self.surname)
        print('Ставка:', self.rate)
        print('Кол-во отработанных дней:', self.days)
        print(f'Зарплата: {self.GetSalary()}\n')
worker1 = Worker("Кот", "Котов", "100", "5")
worker1.output_info()
worker2 = Worker("Кошечка", "Кошечкина", "200", "10")
worker2.output_info()