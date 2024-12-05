from main import turno
from cowboys.tipos import CowboyFactory
from jogo.observer import Observador

def test_turno():
    jogador1 = CowboyFactory.criar_cowboy("1")
    jogador2 = CowboyFactory.criar_cowboy("2")
    observador = Observador()
    
    jogador1.vida = 20  # Reduzir vida para acelerar o teste
    jogador2.vida = 20
    
    turno(jogador1, jogador2, observador)
    assert jogador1.vida <= 0 or jogador2.vida <= 0
