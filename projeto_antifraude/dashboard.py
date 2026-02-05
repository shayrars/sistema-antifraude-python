import pandas as pd
import matplotlib.pyplot as plt

# Ler relatório
df = pd.read_excel("relatorio_final.xlsx")

# Indicadores principais
total = len(df)
aprovadas = len(df[df["decisao"] == "Aprovar"])
analise = len(df[df["decisao"] == "Análise manual"])
bloqueadas = len(df[df["decisao"] == "Bloquear"])

# Percentuais
pct_aprovadas = (aprovadas / total) * 100
pct_analise = (analise / total) * 100
pct_bloqueadas = (bloqueadas / total) * 100

print("===== DASHBOARD ANTIFRAUDE =====")
print(f"Total de transações: {total}")
print(f"Aprovadas: {aprovadas} ({pct_aprovadas:.2f}%)")
print(f"Análise manual: {analise} ({pct_analise:.2f}%)")
print(f"Bloqueadas: {bloqueadas} ({pct_bloqueadas:.2f}%)")

# Gráfico
labels = ["Aprovadas", "Análise manual", "Bloqueadas"]
valores = [aprovadas, analise, bloqueadas]

#Cria uma nova área de gráfico.
plt.figure()
#Cria um gráfico de barras com eixos
plt.bar(labels, valores)
plt.title("Distribuição das decisões antifraude")
plt.xlabel("Decisão")
plt.ylabel("Quantidade")
#Mostra o gráfico na tela.
plt.show()