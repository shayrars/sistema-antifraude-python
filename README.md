📊 Sistema Antifraude em Python

Projeto prático de desenvolvimento de um sistema antifraude completo, simulando um ambiente real de análise de risco, automação de dados e visualização de indicadores.

🎯 Objetivo

Criar uma solução capaz de:

Gerar bases sintéticas realistas de transações

Calcular score antifraude (0–100)

Classificar transações por nível de risco

Automatizar decisões operacionais

Gerar relatórios e dashboards visuais

🏗️ Arquitetura do Projeto

O projeto está organizado em três módulos principais:

gerar_base.py → Gera a base de dados sintética com transações de exemplo

motor_risco.py → Calcula o score antifraude, classifica o risco e aplica regras automáticas

dashboard.py → Cria gráficos, relatórios e dashboards para visualização dos resultados

💡 Em outras palavras: você primeiro cria os dados, depois aplica o motor antifraude e, por fim, visualiza os resultados no dashboard.

⚙️ Tecnologias

Python

Pandas

Matplotlib

Excel

🚀 Como executar
1️⃣ Gerar base de dados
python gerar_base.py

2️⃣ Rodar motor antifraude
python motor_risco.py

3️⃣ Gerar dashboard
python dashboard.py
