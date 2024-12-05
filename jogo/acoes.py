
class AcaoAtacar:
    def executar(self, atacante, defensor):
        dano = max(0, atacante.ataque - defensor.defesa)
        defensor.vida -= dano
        print(f"{atacante.nome} atacou e causou {dano} de dano!")

class AcaoDefender:
    def executar(self, defensor):
        defensor.vida += 5
        print(f"{defensor.nome} se defendeu e recuperou 5 de vida!")

class AcaoHabilidade:
    def executar(self, atacante, defensor):
        dano = atacante.habilidade_especial()
        defensor.vida -= dano
