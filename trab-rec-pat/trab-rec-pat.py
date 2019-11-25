import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

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

print(df.groupby(df['date'].dt.strftime('%m'))['Total do conhec.'].sum())
