class Train:
    def __init__(self,destination,numtrain,departuretime):
        self.destination = destination
        self.numtrain = numtrain
        self.departuretime = departuretime

    def output_info(self):
        print("Название пункта назначения:",self.destination)
        print("Номер поезда:", self.numtrain)
        print("Время отправления:", self.departuretime)

trains = []
trains.append(Train("Москва", 123, "13:00"))
trains.append(Train("Санкт-Петербург", 456, "16:30"))
trains.append(Train("Казань", 789, "19:30"))

def find():
    for train in trains:
        if train.numtrain == train_number:
            train.output_info()
            return "Информация найдена"
    return "Поезд не найден"
print(find())