
class Observador:
    def notificar_vitoria(self, vencedor):
        print(f"{vencedor} venceu a batalha!")

    def notificar_vida(self, cowboy):
        print(f"{cowboy} tem agora {cowboy.vida} pontos de vida.")
