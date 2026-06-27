<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue" alt="Python 3.7+">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License">
</p>

<h1 align="center">🏃 PACE-CLI</h1>
<p align="center"><i>Calculadora de pace para corredores direto do terminal</i></p>

---

## Sobre

O **PACE-CLI** é uma ferramenta de terminal simples e rápida para corredores registrarem seus treinos e consultarem o pace médio (min/km) de cada corrida. Os dados são armazenados localmente em um banco SQLite — sem necessidade de cadastro, internet ou instalação complexa.

---

## Funcionalidades

- **Cadastrar corrida** — informe data, tipo, distância (km) e duração (minutos/segundos)
- **Ver histórico** — visualize todas as corridas registradas com o pace calculado automaticamente
- **Deletar corrida** — remova um registro pelo ID
- **Banco local SQLite** — dados salvos no arquivo `pace.db`

---

## Pré-requisitos

- **Python 3.7+** (apenas bibliotecas padrão: `sqlite3`, `datetime`, `sys`)

Nenhum pacote externo é necessário.

---

## Como usar

```bash
python3 cli.py
```

Um menu interativo será exibido:

```
==============================
      SISTEMA DE CORRIDA      
==============================
1 - Cadastrar nova corrida
2 - Ver histórico de paces
3 - Deletar uma corrida
4 - Sair
Escolha uma opção:
```

Basta digitar o número da opção desejada e seguir as instruções na tela.

### Exemplo

```
Escolha uma opção: 1

--- Cadastro de Corrida ---
Data (AAAA-MM-DD): 2024-06-27
Tipo (Ex: Corrida na rua): Corrida Esteira
Distância (km): 5
Minutos: 25
Segundos: 30
Sucesso: Dados salvos!
```

```
Escolha uma opção: 2

--- Histórico de Paces ---
[ID: 1] Na corrida do dia 2024-06-27, o pace foi de 5 Minutos e 6 Segundos
```

> O banco `pace.db` é criado no diretório onde o script for executado.

---

## Estrutura do banco de dados

| Coluna | Tipo | Descrição |
|---|---|---|
| `id` | INTEGER (PK) | Identificador único |
| `data_sessao` | TEXT | Data da corrida (AAAA-MM-DD) |
| `tipo` | TEXT | Descrição do treino |
| `distancia_km` | REAL | Distância percorrida em km |
| `duracao_segundos` | INTEGER | Duração total em segundos |

---

## Autor

Desenvolvido por [@KauaRios](https://github.com/KauaRios)

---

## Licença

Distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais informações.
