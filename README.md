# 🎮 JOKENPÔ ARENA

Jogo de **Pedra, Papel e Tesoura** com visual de game moderno (dark mode, neon e glassmorphism), feito com **Python + Flask**, **Programação Orientada a Objetos** e uma **API REST**. Toda a lógica do jogo roda no backend; o front-end apenas envia a jogada e desenha o resultado.

![Screenshot da tela inicial](docs/screenshot-home.png)
![Screenshot da arena](docs/screenshot-arena.png)

> 📸 Espaço reservado: rode o projeto, tire os prints e salve em `docs/` com esses nomes.

## 🎯 Objetivo do jogo

Escolha **pedra**, **papel** ou **tesoura** e vença o computador:

- ✊ Pedra quebra ✌️ Tesoura
- ✋ Papel cobre ✊ Pedra
- ✌️ Tesoura corta ✋ Papel

## ✨ Funcionalidades

- Tela inicial com logo, botão **JOGAR AGORA**, regras e estatísticas (partidas, vitórias, derrotas).
- **Melhor de 1**: uma rodada decide; empate repete a rodada.
- **Melhor de 5**: até 5 rodadas, vence quem fizer **3 vitórias** primeiro (encerra automaticamente).
- Placar em tempo real, indicador de rodada, bolinhas de progresso e histórico de jogadas.
- Botões de reiniciar e voltar ao menu; atalhos de teclado `1` (pedra), `2` (papel), `3` (tesoura).
- Animações: confete e brilho na vitória, impacto e vermelho na derrota, efeito próprio no empate.
- Design responsivo (computador, tablet e celular).
- Estatísticas salvas em `data/estatisticas.json`.

> **Regra de empate:** empates não consomem rodada. Por isso, no Melhor de 5, a partida sempre termina com um vencedor (3 x 0, 3 x 1 ou 3 x 2).

## 🧰 Tecnologias

Python 3 · Flask · HTML5 · CSS3 · JavaScript (puro) · API REST · unittest · Git/GitHub

## 📁 Estrutura de pastas

```
jokenpo-arena/
├── app.py                 # Flask: rotas da API REST e página principal
├── jokenpo/
│   ├── __init__.py
│   └── models.py          # Classes POO: Jogador, Computador, Partida, Jogo
├── templates/index.html   # Página única (home + arena)
├── static/
│   ├── css/style.css      # Tema neon, glassmorphism, animações
│   └── js/app.js          # Consome a API e controla a interface/efeitos
├── tests/test_jogo.py     # Testes automatizados
├── data/                  # Estatísticas (arquivo gerado em execução)
├── requirements.txt
└── README.md
```

## 🧱 Classes (POO)

| Classe | Responsabilidade |
|---|---|
| `Jogador` | Guarda nome, escolha atual e vitórias em **atributos privados** (`__nome`, `__escolha`, `__vitorias`), acessados por propriedades. Valida a jogada em `escolher()`. |
| `Computador` | **Herda** de `Jogador` e implementa `jogar()`, escolhendo aleatoriamente. Aceita um gerador injetável (facilita testes). |
| `Partida` | Controla rodadas, placar, histórico e o **encerramento automático** (1 vitória no Melhor de 1, 3 no Melhor de 5). |
| `Jogo` | Administra as regras, as partidas em andamento (por ID) e as estatísticas gerais. |

Conceitos aplicados: encapsulamento, herança, separação de responsabilidades, organização modular e validação no backend (`JogadaInvalidaError`, `PartidaNaoEncontradaError`, `PartidaFinalizadaError`).

## ⚙️ Como o backend funciona

1. O front chama `POST /api/partidas` com o modo; o `Jogo` cria uma `Partida` e devolve o estado com um `id`.
2. A cada clique, o front envia `POST /api/partidas/<id>/jogadas` com `{"escolha": "pedra"}`.
3. A `Partida` valida a jogada, sorteia a do computador, decide o resultado, atualiza o placar e verifica se acabou.
4. O servidor responde com a rodada, o estado completo da partida e as estatísticas; o front só desenha.

## 🔌 Endpoints da API

| Método | Rota | Descrição |
|---|---|---|
| GET | `/api/regras` | Opções, quem vence quem e modos disponíveis |
| GET | `/api/estatisticas` | `{partidas, vitorias, derrotas}` |
| POST | `/api/partidas` | Cria partida. Body: `{"modo": "melhor_de_1" \| "melhor_de_5"}` → `201` |
| GET | `/api/partidas/<id>` | Estado atual da partida |
| POST | `/api/partidas/<id>/jogadas` | Joga uma rodada. Body: `{"escolha": "pedra" \| "papel" \| "tesoura"}` |

Erros em JSON: `400` jogada/modo inválido · `404` partida inexistente · `409` partida já encerrada.

Exemplo:

```bash
curl -X POST http://127.0.0.1:5000/api/partidas -H "Content-Type: application/json" -d '{"modo":"melhor_de_5"}'
```

## 🚀 Instalação e execução

Requer Python 3.9+.

```bash
git clone https://github.com/SEU-USUARIO/jokenpo-arena.git
cd jokenpo-arena

python -m venv .venv
# Windows:  .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Abra **http://127.0.0.1:5000** no navegador.

## ✅ Testes

```bash
python -m unittest -v
```

Cobrem: todas as combinações de regras, validação de jogadas, Melhor de 1 (inclusive empate), Melhor de 5 (3 x 0, 3 x 2, vitória do computador), placar, encerramento automático, estatísticas e a API (fluxo completo e códigos de erro).

## 👤 Autor

**Lucas Mendes Aguiar** — estudante de T.I & Desenvolvimento de Sistemas.
