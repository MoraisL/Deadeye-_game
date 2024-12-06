# 🤠 Deadeye game

Cowboys Bebolas é um jogo de combate por turnos desenvolvido para rodar no console. Ele permite que dois jogadores (ou um jogador contra a IA) escolham cowboys com habilidades únicas e se enfrentem até que apenas um permaneça de pé. O projeto utiliza cinco padrões de design para garantir um código modular, fácil de entender e pronto para extensões futuras.

## 🎯 Estrutura do Projeto

- **main.py**: Arquivo principal que gerencia o fluxo do jogo, exibe o menu e inicia as partidas.
- **/cowboys**: Contém as classes dos cowboys e a **Factory** responsável por criar as instâncias.
  - **cowboy.py**: Define a classe abstrata `Cowboy`.
  - **tipos.py**: Implementa várias classes de cowboys com habilidades específicas e a `CowboyFactory`.
- **/jogo**: Contém a lógica de ações, estado do jogo, sistema de salvamento e observadores.
  - **acoes.py**: Implementa o **Strategy Pattern** para ações como atacar, defender e usar habilidades.
  - **estado.py**: Implementa o **Singleton Pattern** para gerenciar a pontuação global e o progresso.
  - **memento.py**: Implementa o **Memento Pattern** para salvar e carregar o progresso do jogo.
  - **observer.py**: Implementa o **Observer Pattern** para monitorar mudanças e vitórias.

## 🔍 Padrões de Design Utilizados

1. **Factory Pattern** (tipos.py)
   - Usado para criar dinamicamente diferentes tipos de cowboys com base na escolha do jogador.
   - Exemplo: `CowboyFactory.criar_cowboy(tipo)` cria um cowboy com as habilidades correspondentes.

2. **Strategy Pattern** (acoes.py)
   - Define diferentes estratégias de ação, como `Atacar`, `Defender` e `HabilidadeEspecial`.
   - Permite alternar facilmente entre diferentes ações durante o jogo.

3. **Singleton Pattern** (estado.py)
   - Garante que o estado do jogo (como pontuações e progresso) seja compartilhado globalmente por toda a aplicação.
   - Exemplo: `GameState()` sempre retorna a mesma instância do estado global.

4. **Observer Pattern** (observer.py)
   - Notifica os jogadores sobre eventos importantes, como mudanças na vida dos cowboys ou vitórias.
   - Exemplo: `observador.notificar_vida(cowboy)` exibe uma mensagem sempre que a vida muda.

5. **Memento Pattern** (memento.py)
   - Permite salvar e restaurar o progresso do jogo.
   - Exemplo: `Memento.salvar(estado)` salva o estado atual, e `Memento.carregar()` restaura um estado salvo anteriormente.

## ⚙️ Como Funciona o Jogo

1. **Escolha do Modo de Jogo**:
   - PvP: Dois jogadores humanos escolhem seus cowboys.
   - PvE: Um jogador enfrenta a IA (que escolhe ações aleatórias).

2. **Escolha dos Cowboys**:
   - O jogador escolhe entre cinco tipos de cowboys, cada um com uma habilidade especial:
     - **Atirador Rápido**: Dispara duas vezes.
     - **Defensor Fortificado**: Recupera vida ao se defender.
     - **Cowboy Aleatório**: Causa dano imprevisível.
     - **Cowboy Explosivo**: Lança dinamite e causa dano massivo.
     - **Cowboy Veloz**: Aumenta o ataque ao longo do tempo.

3. **Combate por Turnos**:
   - A cada turno, um jogador (ou IA) pode **atacar**, **defender** ou usar **habilidade especial**.
   - O jogo alterna entre os jogadores até que um dos cowboys perca toda a vida.

4. **Sistema de Pontuação e Salvamento**:
   - O jogo mantém a pontuação dos jogadores usando o **Singleton Pattern**.
   - O progresso pode ser salvo e carregado a qualquer momento com o **Memento Pattern**.

Aqui está o README atualizado com as instruções completas de execução, incluindo o uso de um ambiente virtual (`venv`) e a instalação de dependências:

## 🛠️ Como Executar

### 1. Preparar o Ambiente

1. Certifique-se de ter o [Python 3.10 ou superior](https://www.python.org/downloads/) instalado em sua máquina.
2. Extraia o projeto do arquivo ZIP.
3. Abra o terminal ou prompt de comando e navegue até a pasta do projeto.

### 2. Criar e Ativar o Ambiente Virtual

1. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```
2. Ative o ambiente virtual:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/Mac**:
     ```bash
     source venv/bin/activate
     ```

### 3. Instalar Dependências

1. Com o ambiente virtual ativado, instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

### 4. Executar o Jogo

1. Ainda no terminal, execute o arquivo principal para iniciar o jogo:
   ```bash
   python main.py
   ```

---

## 🧪 Como Executar os Testes

1. Certifique-se de que o ambiente virtual esteja ativado (veja a etapa anterior).
2. Navegue até a pasta de testes:
   ```bash
   cd tests
   ```
3. Execute os testes com o `pytest`:
   ```bash
   pytest
   ```

   - Para desabilitar a captura de saída e permitir interação com `stdin`, use:
     ```bash
     pytest -s
     ```

---

## 🚀 Notas Adicionais

- Sempre ative o ambiente virtual antes de executar o jogo ou os testes.
- Se precisar instalar novas dependências, use `pip install` e atualize o arquivo `requirements.txt` com:
  ```bash
  pip freeze > requirements.txt
  ```
- Para desativar o ambiente virtual, use:
  ```bash
  deactivate
  ```

# Boa diversão!
