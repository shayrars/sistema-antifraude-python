import pandas as pd

df =pd.read_excel("transacoes.xlsx")

def decidir_linha(linha):
    risco = 0

    # Valor alto
    if linha["valor"] > 5000:
        risco += 25

    # Cliente novo
    if linha["cliente"] == "s":
        risco += 20

    # Score baixo
    if linha["score"] < 40:
        risco += 30
    elif linha["score"] < 60:
        risco += 10

    # Madrugada
    if 0 <= linha["hora"] <= 5:
        risco += 15

    # Histórico de chargebacks
    if linha["chargebacks"] >= 3:
        risco += 20
    elif linha["chargebacks"] == 2:
        risco += 10

    # Limitar score máximo
    if risco > 100:
        risco = 100

    # Definir nível de risco
    if risco >= 70:
        nivel = "Crítico"
    elif risco >= 50:
        nivel = "Alto"
    elif risco >= 30:
        nivel = "Médio"
    else:
        nivel = "Baixo"

    # Tomada de decisão
    if risco >= 60:
        decisao = "Bloquear"
    elif risco >= 30:
        decisao = "Análise manual"
    else:
        decisao = "Aprovar"

    return risco, nivel, decisao

# Aplicar regras e criar novas colunas
df[["score_risco", "nivel_risco", "decisao"]] = df.apply(
    decidir_linha, axis=1, result_type="expand"
)

# Salvar relatório
df.to_excel("relatorio_final.xlsx", index=False)

print("Relatório gerado com sucesso: relatorio_final.xlsx")