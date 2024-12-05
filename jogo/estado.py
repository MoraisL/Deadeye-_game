
class GameState:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameState, cls).__new__(cls)
            cls._instance.pontuacao = {}
        return cls._instance

    def adicionar_pontuacao(self, jogador):
        self.pontuacao[jogador] = self.pontuacao.get(jogador, 0) + 1
