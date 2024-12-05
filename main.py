
from cowboys.tipos import CowboyFactory
from jogo.acoes import AcaoAtacar, AcaoDefender, AcaoHabilidade
from jogo.estado import GameState
from jogo.memento import Memento
from jogo.observer import Observador
import random
import time

def mostrar_status(jogador1, jogador2):
    print(f"🧍 {jogador1.nome}: {jogador1.vida} HP | 🧍 {jogador2.nome}: {jogador2.vida} HP\n")

def turno(jogador1, jogador2, observador):
    jogadores = [jogador1, jogador2]
    random.shuffle(jogadores)

    while jogador1.vida > 0 and jogador2.vida > 0:
        for jogador in jogadores:
            defensor = jogador2 if jogador == jogador1 else jogador1
            mostrar_status(jogador1, jogador2)

            if jogador.vida <= 0:
                continue

            if jogador == jogador1:
                acao = input(f"🎯 {jogador.nome}, escolha sua ação (1 - Atacar, 2 - Defender, 3 - Habilidade Especial): ")
            else:
                acao = str(random.choice([1, 2, 3]))
                print(f"🤖 O robô escolheu a ação: {acao}")
                time.sleep(1)

            if acao == '1':
                AcaoAtacar().executar(jogador, defensor)
            elif acao == '2':
                AcaoDefender().executar(jogador)
            elif acao == '3':
                AcaoHabilidade().executar(jogador, defensor)

            observador.notificar_vida(defensor)

            if defensor.vida <= 0:
                print(f"🏆 {jogador.nome} venceu a batalha!")
                GameState().adicionar_pontuacao(jogador.nome)
                observador.notificar_vitoria(jogador.nome)
                return

def menu():
    observador = Observador()
    estado = GameState()

    while True:
        print("\n===== 🤠 Cowboys Bebolas =====")
        opcao = input("1 - Novo Jogo (PvP) | 2 - Novo Jogo (PvE) | 3 - Carregar Jogo | 4 - Sair: ")

        if opcao in ['1', '2']:
            jogador1 = CowboyFactory.criar_cowboy(
                input("Escolha seu cowboy (1-Atirador, 2-Defensor, 3-Aleatório, 4-Explosivo, 5-Veloz): ")
            )
            if opcao == '1':
                jogador2 = CowboyFactory.criar_cowboy(input("Escolha o cowboy adversário: "))
            else:
                jogador2 = CowboyFactory.criar_cowboy(str(random.choice(['1', '2', '3', '4', '5'])))

            if jogador1 and jogador2:
                turno(jogador1, jogador2, observador)
            else:
                print("⚠️ Escolha inválida de cowboy.")

        elif opcao == '3':
            estado = Memento.carregar() or estado

        elif opcao == '4':
            Memento.salvar(estado)
            print("💾 Jogo salvo e encerrado.")
            break

if __name__ == "__main__":
    menu()
