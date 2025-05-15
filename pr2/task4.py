class Number:
    def __init__(self, value = 0):
        self.value = value
    def increase(self):
        self.value += 1
    def decrease(self):
        self.value -= 1
    def output_info(self):
        return self.value
counter = Number()
print(f"Начальное значение: {counter.output_info()}")
counter.increase()
print(f"Значение после увеличения: {counter.output_info()}")
counter.decrease()
print(f"Значение после уменьшения: {counter.output_info()}")

counter2 = Number(value = 5)
print(f"Начальное значение: {counter2.output_info()}")
counter2.increase()
print(f"Значение после увеличения: {counter2.output_info()}")
counter2.decrease()
print(f"Значение после уменьшения: {counter2.output_info()}")