import pytest
from cowboys.tipos import AtiradorRapido, DefensorFortificado, CowboyAleatorio, CowboyExplosivo, CowboyVeloz

def test_atirador_rapido():
    cowboy = AtiradorRapido("Test Atirador")
    assert cowboy.habilidade_especial() == cowboy.ataque * 2

def test_defensor_fortificado():
    cowboy = DefensorFortificado("Test Defensor")
    initial_vida = cowboy.vida
    cowboy.habilidade_especial()
    assert cowboy.vida == initial_vida + 10

def test_cowboy_aleatorio():
    cowboy = CowboyAleatorio("Test Aleatório")
    dano = cowboy.habilidade_especial()
    assert 5 <= dano <= 20

def test_cowboy_explosivo():
    cowboy = CowboyExplosivo("Test Explosivo")
    assert cowboy.habilidade_especial() == 25

def test_cowboy_veloz():
    cowboy = CowboyVeloz("Test Veloz")
    initial_ataque = cowboy.ataque
    resultado = cowboy.habilidade_especial()
    assert cowboy.ataque == initial_ataque + 5
    assert resultado == cowboy.ataque
