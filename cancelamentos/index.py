import pandas as pd

tabela = pd.read_csv("cancelamentos.csv")
tabela = tabela.drop("CustomerID", axis=1)
display(tabela)

# Identificamento e removendo valores vazios
display(tabela.info())
tabela = tabela.dropna()
display(tabela.info())

# Quantas pessoas cancelaram e não cancelaram
display(tabela['cancelou'].value_counts())
display(tabela['cancelou'].value_counts(normalize=True).map("{:.1%}").__format__)

display(tabela["duracao_contrato"].value_counts(normalize=True))
display(tabela["duracao_contrato"].value_counts())

# Analisando o contrato mensal
display(tabela.groupby("duracao_contrato").mean(numeric_only=True))
# Descobrimos aqui que a média de cancelamentos é 1, ou seja, praticamente todos os contratos mensais cancelaram (ou todos)

# Então descobrimos que contrato mensal é ruim, vamos tirar ele e continuar analisando
tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
display(tabela)
display(tabela)
display(tabela['cancelou'].value_counts())
display(tabela['cancelou'].value_counts(normalize=True).map("{:.1%}").__format__)

# Chegamos agora em menos da metades das pessoas cancelando, mas ainda temos tem muitas pessoas ai, vamos continuar analisando
display(tabela["assinatura"].value_counts(normalize=True))
display(tabela.groupby("assinatura").mean(numeric_only=True))
# Vemos que assinatura é quase 1/3, 1/3, 1/3
# e que os cancelamentos são os na média bem parecidos, então fica difícil tirar alguma conclusão da média, vamos precisar ir mais a fundo

# Vamos criar gráfico, porque só com números tá difícil de visualizar
import plotly.express as px

for coluna in tabela.columns
    grafico = px.histogram(tabela, x=coluna, color="cancelamentos")
    grafico.show()