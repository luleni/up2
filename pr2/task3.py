class Numbers:
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2
    def output_info(self):
        print('Первое число:', self.num1)
        print(f'Второе число:{self.num2}\n')
    def change(self, new_num1, new_num2):
        self.num1 = new_num1
        self.num2 = new_num2
    def sum(self):
        return self.num1 + self.num2
    def max(self):
        return max(self.num1, self.num2)
numbers = Numbers(3,5)
numbers.output_info()
numbers.change(10,4)
numbers.output_info()
print('Сумма чисел:', numbers.sum())
print('Наибольшее число:', numbers.max())