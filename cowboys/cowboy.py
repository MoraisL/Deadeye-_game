
from abc import ABC, abstractmethod

class Cowboy(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.ataque = 10
        self.defesa = 5

    @abstractmethod
    def habilidade_especial(self):
        pass

    def __str__(self):
        return f"{self.nome} (Vida: {self.vida})"
