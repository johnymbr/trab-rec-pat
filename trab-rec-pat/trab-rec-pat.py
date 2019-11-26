import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
pd.options.display.float_format = '{:.2f}'.format

df = pd.read_csv('cte2018.csv', sep=';')

# Agrupar por "Mercadoria grupo"
# df["Mercadoria grupo"].value_counts().plot.barh()
# plt.show()

# Agrupar os valores de conhecimento por Mes.
# df['date'] = pd.to_datetime(df['Data emissão'])
# df.groupby(df['date'].dt.strftime('%m'))['Total do conhec.'].sum().plot()
# plt.ticklabel_format(style='plain', axis='y')
# plt.grid('on', which='minor', axis='x')
# plt.grid('off', which='major', axis='x')
# plt.xlabel('Meses')
# plt.ylabel('Valores')
# plt.show()

# Agrupar os valores por "UF da entrega"
# ax1 = df.groupby(["UF da entrega"])["Peso carregado"].agg('sum').plot(color='blue', grid=True, label='Peso', kind="bar")
# ax2 = df.groupby(["UF da entrega"])["Total do conhec."].agg('sum').plot(color='red', secondary_y=True, label='Valor', kind="bar")
#
# ax1.legend(loc=1)
# ax1.ticklabel_format(style='plain', axis='y')
# ax1.set_ylabel('Peso')
# ax2.legend(loc=2)
# ax2.ticklabel_format(style='plain', axis='y')
# ax2.set_ylabel('Valor')
#
# plt.grid('on', which='minor', axis='x')
# plt.grid('off', which='major', axis='x')
# plt.xlabel('Estados Entrega')
# plt.show()

# Agrupar os valores por "Mes" e "UF da entrega"
df['date'] = pd.to_datetime(df['Data emissão'])
ax1 = df.groupby([df['date'].dt.strftime('%m'), "UF da entrega"])["Peso carregado"].agg('sum').plot(color='blue', grid=True, label='Peso', kind="bar")
plt.ticklabel_format(style='plain', axis='y')
plt.grid('on', which='minor', axis='x')
plt.grid('off', which='major', axis='x')
plt.xlabel('Mes / UF')
plt.ylabel('Peso')
plt.show()
