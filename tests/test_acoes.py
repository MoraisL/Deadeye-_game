import pytest 
from jogo.acoes import AcaoAtacar, AcaoDefender, AcaoHabilidade
from cowboys.tipos import AtiradorRapido, DefensorFortificado

def test_acao_atacar():
    atacante = AtiradorRapido("Atacante")
    defensor = DefensorFortificado("Defensor")
    initial_vida = defensor.vida
    AcaoAtacar().executar(atacante, defensor)
    dano = max(0, atacante.ataque - defensor.defesa)
    assert defensor.vida == initial_vida - dano

def test_acao_defender():
    defensor = DefensorFortificado("Defensor")
    initial_vida = defensor.vida
    AcaoDefender().executar(defensor)
    assert defensor.vida == initial_vida + 5

def test_acao_habilidade():
    atacante = AtiradorRapido("Atacante")
    defensor = DefensorFortificado("Defensor")
    initial_vida = defensor.vida
    dano = atacante.habilidade_especial()
    AcaoHabilidade().executar(atacante, defensor)
    assert defensor.vida == initial_vida - dano
