# ⚓ Batalha Naval

Projeto de **Batalha Naval** desenvolvido em **Python** como trabalho da faculdade.

O jogo é **single-player** e tem como objetivo afundar todas as embarcações posicionadas automaticamente no tabuleiro.  
Ao final da partida, a quantidade de jogadas utilizadas é salva em um **ranking**, que pode ser consultado pelo jogador.

---

## 🎮 Sobre o jogo

- O tabuleiro é gerado automaticamente
- Existem dois tipos de embarcação:
  - **Navio** (1 posição)
  - **Submarino** (2 posições)
- O jogador tenta acertar todas as embarcações
- O jogo contabiliza o número de jogadas
- Ao vencer, o desempenho é salvo em um ranking

---

## 🛠 Tecnologias utilizadas

- **Linguagem:** Python
- **Bibliotecas:**  
  - `random`  
  - `string`  
(Bibliotecas padrão da linguagem)

---

## 📁 Estrutura do projeto

O projeto é dividido em **4 arquivos principais**, cada um com uma responsabilidade específica:

### 🔹 `Tabuleiro.py`
Contém a classe `Tabuleiro`, responsável por:
- Criar o tabuleiro do jogo
- Posicionar as embarcações de forma aleatória
- Gerenciar toda a lógica interna relacionada ao tabuleiro

> ⚠️ **Importante:**  
> O módulo **Tabuleiro** foi fornecido pela **faculdade**.  
> Todos os direitos sobre esse módulo pertencem à instituição de ensino.

---

### 🔹 `Exibicao.py`
Responsável por toda a **parte visual e mensagens do jogo**, incluindo:
- Exibição do tabuleiro para o jogador
- Atualização visual conforme tiros acertam água ou embarcações
- Mensagens do menu, instruções e feedbacks do jogo

A lógica visual é separada da lógica interna do tabuleiro.

---

### 🔹 `Persistencia.py`
Responsável pelo **ranking**, incluindo:
- Salvamento da quantidade de jogadas
- Leitura e exibição do ranking
- Armazenamento dos dados no arquivo `ranking.txt`

---

### 🔹 `FrontEnd.py`
Arquivo principal do jogo, onde:
- O menu principal é exibido
- O jogador pode:
  - Iniciar um novo jogo
  - Visualizar o ranking
  - Sair do jogo
- Toda a lógica da partida acontece
- O jogador pode desistir e retornar ao menu

---

## ▶️ Como executar o jogo

1. Clone este repositório:
   ```bash
   git clone <url-do-repositorio>
2. Acesse a pasta do projeto
3. Execute o arquivo main.py
4. O jogo iniciará automaticamente pelo menu principal

---

## 💡 Funcionalidades

- Posicionamento automático das embarcações
- Contagem de jogadas
- Sistema de ranking persistente
- Menu interativo
- Separação entre lógica do jogo e exibição visual

---

## 📸 Capturas de tela

(A ser adicionado)

---

## 📚 Créditos

- Módulo Tabuleiro desenvolvido e fornecido pela faculdade
- Demais módulos e integração desenvolvidos por mim como parte do projeto acadêmico

---

## 📌 Próximos passos / melhorias

Corrigir leitura do ranking
