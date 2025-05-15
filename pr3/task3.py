class Calculation:
    def __init__(self):
        self.calculationLine = ""
    def SetCalculation(self,newLine):
        self.calculationLine = str(newLine)
        return newLine
    def SetLastSymbolCalculationLine(self, symbol):
        self.calculationLine += str(symbol)
    def GetCalculationLine(self):
        return self.calculationLine
    def GetLastSymbol(self):
        return self.calculationLine[-1]
    def DeleteLastSymbol(self):
        self.calculationLine = self.calculationLine[:-1]
        return self.calculationLine
calc = Calculation()
print('Начальная строка:',
      calc.GetCalculationLine())
print('Строка после изменения:',
      calc.SetCalculation(12345))
calc.SetLastSymbolCalculationLine(6)
print('Последний символ:',
      calc.GetLastSymbol())
print('Строка после удаления последнего символа:',
      calc.DeleteLastSymbol())
print('Строка после изменений:',
      calc.GetCalculationLine())