def __init__(self, nombre, fichas=5):
    self.nombre = nombre
    self.fichas = fichas

def __str__(self):
    return f"{self.nombre}, {self.fichas} fichas"

def darFichas(self, cuantas=1):
    self.fichas += cuantas

def sacarFichas(self, cuantas=1):
    if cuantas > self.fichas:
        raise ValueError()