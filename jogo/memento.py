
import pickle

class Memento:
    @staticmethod
    def salvar(estado, arquivo='salvo.pkl'):
        with open(arquivo, 'wb') as f:
            pickle.dump(estado, f)

    @staticmethod
    def carregar(arquivo='salvo.pkl'):
        try:
            with open(arquivo, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("Nenhum jogo salvo encontrado.")
            return None
