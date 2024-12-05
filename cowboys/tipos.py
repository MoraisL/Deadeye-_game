
from .cowboy import Cowboy
import random

class AtiradorRapido(Cowboy):
    def habilidade_especial(self):
        print(f"🔫 {self.nome} dispara duas vezes rapidamente!")
        return self.ataque * 2

class DefensorFortificado(Cowboy):
    def habilidade_especial(self):
        print(f"🛡️ {self.nome} se defende e recupera 10 pontos de vida!")
        self.vida += 10
        return 0

class CowboyAleatorio(Cowboy):
    def habilidade_especial(self):
        dano = random.randint(5, 20)
        print(f"🎲 {self.nome} causa um dano aleatório de {dano}!")
        return dano

class CowboyExplosivo(Cowboy):
    def habilidade_especial(self):
        print(f"💥 {self.nome} joga dinamite, causando uma explosão!")
        return 25

class CowboyVeloz(Cowboy):
    def habilidade_especial(self):
        print(f"⚡ {self.nome} ataca rápido e aumenta seu ataque!")
        self.ataque += 5
        return self.ataque

class CowboyFactory:
    @staticmethod
    def criar_cowboy(tipo):
        tipos = {
            "1": AtiradorRapido("Atirador Rápido"),
            "2": DefensorFortificado("Defensor Fortificado"),
            "3": CowboyAleatorio("Cowboy Aleatório"),
            "4": CowboyExplosivo("Cowboy Explosivo"),
            "5": CowboyVeloz("Cowboy Veloz")
        }
        return tipos.get(tipo, None)
