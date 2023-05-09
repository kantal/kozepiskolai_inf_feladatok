# A csharp.txt átirata Pythonban

class EredményElemző:

    def DöntetlenekSzáma(self):
            return self.Megszámol('X')

    def Megszámol(self, kimenet):
            return self.Eredmények.count(kimenet)

    def NemvoltDöntetlenMérkőzés(self):
            return self.DöntetlenekSzáma() == 0

    def __init__(self,eredmény):  # konstruktor
        self.Eredmények= eredmény
