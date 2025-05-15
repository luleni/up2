class Class:
    def __init__(self, value1 = 0, value2 = 0):
        if value1 == 0 and value2 == 0:
            self.value1 = value1
            self.value2 = value2
            print("--Объект создан со значениями по умолчанию--")
        else:
            self.value1 = value1
            self.value2 = value2
            print("--Объект создан с параметрами--")
    def __del__(self):
        print("Объект удален =(")

obj1 = Class()
print("первое значение по умолчанию:", obj1.value1)
print(f"второе значение по умолчанию: {obj1.value2}\n")

obj2 = Class(456, 123)
print("первое значение с параметрами:", obj2.value1)
print(f"второе значение с параметрами: {obj2.value2}\n")