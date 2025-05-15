class Worker:
    def __init__(self,name,surname,rate,days):
        self.__name = name
        self.__surname = surname
        self.__rate = int(rate)
        self.__days = int(days)
    def name_get(self):
        return self.__name
    def surname_get(self):
        return self.__surname
    def rate_get(self):
        return self.__rate
    def days_get(self):
        return self.__days
    def GetSalary(self):
        salary = self.__rate * self.__days
        return salary
    def output_info(self):
        print('Имя:',self.name_get())
        print('Фамилия:', self.surname_get())
        print('Ставка:', self.rate_get())
        print('Кол-во отработанных дней:', self.days_get())
        print(f'Зарплата: {self.GetSalary()}\n')
worker1 = Worker("Кот", "Котов", "100", "5")
worker1.output_info()
worker2 = Worker("Кошечка", "Кошечкина", "200", "10")
worker2.output_info()