# Importa a biblioteca pandas, usada para trabalhar com tabelas/planilhas
import pandas as pd

# Importa a biblioteca random, usada para gerar números aleatórios
import random

# Lista vazia que vai armazenar todas as transações
dados = []

# Loop que será executado 1000 vezes (vai gerar 1000 transações)
for _ in range(1000):

    # Gera um valor aleatório da transação entre 10 e 15000
    # round(..., 2) arredonda para 2 casas decimais
    valor = round(random.uniform(10, 15000), 2)

    # Escolhe aleatoriamente se o cliente é novo ("s") ou não ("n")
    cliente = random.choice(["s", "n"])

    # Gera um score inteiro aleatório entre 10 e 100
    score = random.randint(10, 100)

    # Gera uma hora aleatória entre 0 e 23
    hora = random.randint(0, 23)

    # Gera quantidade de chargebacks, com maior chance para valores baixos
    # weights define a probabilidade de cada valor aparecer
    chargebacks = random.choices(
        [0, 1, 2, 3, 4],      # valores possíveis
        weights=[60, 20, 10, 7, 3]  # probabilidades em %
    )[0]

    # Adiciona uma linha de dados na lista
    dados.append([valor, cliente, score, hora, chargebacks])

# Converte a lista em uma tabela (DataFrame)
df = pd.DataFrame(dados, columns=[
    "valor",
    "cliente",
    "score",
    "hora",
    "chargebacks"
])

# Salva a tabela em um arquivo Excel chamado transacoes.xlsx
# index=False remove a coluna de índice automático
df.to_excel("transacoes.xlsx", index=False)

# Mensagem final informando sucesso
print("Base gerada com sucesso: transacoes.xlsx")