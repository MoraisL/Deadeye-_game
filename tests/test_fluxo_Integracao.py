from main import turno
from cowboys.tipos import CowboyFactory
from jogo.observer import Observador

def test_turno(monkeypatch):
    jogador1 = CowboyFactory.criar_cowboy("1")
    jogador2 = CowboyFactory.criar_cowboy("2")
    observador = Observador()

    jogador1.vida = 20  # Reduzir vida para acelerar o teste
    jogador2.vida = 20

    # Simular entradas para as ações
    inputs = iter(["1", "2", "3"])  # Substitua pelos valores que você quer testar
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    turno(jogador1, jogador2, observador)