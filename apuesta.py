class Apuesta:
    def __init__(self):
        self.fichas = 0
    def __repr__(self):
        return f'Apuesta: {self.fichas} fichas'
    def ponerFicha(self, cuantas=1):
        self.fichas = self.fichas + cuantas 
    def tomarFicha(self, cuantas=1):
        if cuantas > self.fichas:
            raise ValueError(f'no hay tantas fichas (no se puede sacar {cuantas})')
        self.fichas = self.fichas - cuantas 