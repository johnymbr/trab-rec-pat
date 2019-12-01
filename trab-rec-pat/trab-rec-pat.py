import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import seaborn as sns

plt.style.use('ggplot')
pd.options.display.float_format = '{:.2f}'.format

df = pd.read_csv('cte2018.csv', sep=';', decimal=',')

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
# plt.ylabel('Valores (R$)')
# plt.show()

# Agrupar os valores por "UF da entrega"
# ax1 = df.groupby(["UF da entrega"])["Peso carregado"].agg('sum').plot(color='blue', grid=True, label='Peso', kind="bar")
# ax2 = df.groupby(["UF da entrega"])["Total do conhec."].agg('sum').plot(color='red', secondary_y=True, label='Valor', kind="bar")
#
# ax1.legend(loc=1)
# ax1.ticklabel_format(style='plain', axis='y')
# ax1.set_ylabel('Peso (kg)')
# ax2.legend(loc=2)
# ax2.ticklabel_format(style='plain', axis='y')
# ax2.set_ylabel('Valor (R$)')
#
# plt.grid('on', which='minor', axis='x')
# plt.grid('off', which='major', axis='x')
# plt.xlabel('Estados Entrega')
# plt.show()

# Agrupar "Mercadoria grupo" por "Mes"
# df['date'] = pd.to_datetime(df['Data emissão'])
# df.groupby([df['date'].dt.strftime('%m')])["Mercadoria grupo"].value_counts().plot(color='blue', grid=True, label='Peso')
# plt.ticklabel_format(style='plain', axis='y')
# plt.grid('on', which='minor', axis='x')
# plt.grid('off', which='major', import matplotlib.ticker as tkraxis='x')
# plt.xlabel('Mes')
# plt.ylabel('Qtde Grupo Mercadoria')
# plt.show()
df['date'] = pd.to_datetime(df['Data emissão'])
df['date'] = df['date'].dt.strftime('%m')
piv = pd.pivot_table(df, index=['date'], columns=['Mercadoria grupo'], aggfunc='size', fill_value=0)

formatter = tkr.ScalarFormatter(useMathText=True)
formatter.set_scientific(False)

sns.heatmap(piv, annot=True, annot_kws={"size": 8}, cmap='Blues', fmt='.12g', cbar_kws={'format': formatter})

plt.xticks(fontsize=6, rotation=45)
plt.show()

# Agrupar "Mercadoria grupo" por "UF da entrega"
# piv = pd.pivot_table(df, index=['UF da entrega'], columns=['Mercadoria grupo'], aggfunc='size', fill_value=0)
#
# formatter = tkr.ScalarFormatter(useMathText=True)
# formatter.set_scientific(False)
#
# sns.heatmap(piv, annot=True, annot_kws={"size": 8}, cmap='Blues', fmt='.12g', cbar_kws={'format': formatter})
#
# plt.xticks(fontsize=6, rotation=45)
# plt.show()

# Agrupar valor por "Mes" - Grupo Glicerina
# df['date'] = pd.to_datetime(df['Data emissão'])
# ax1 = df[df['Mercadoria grupo'] == 'GLICERINA'].groupby([df['date'].dt.strftime('%m')])["Total do conhec."].agg('sum').plot(color='blue', grid=True, label='Valor', kind="bar")
# ax2 = df[df['Mercadoria grupo'] == 'GLICERINA'].groupby([df['date'].dt.strftime('%m')])["Peso carregado"].agg('sum').plot(color='red', secondary_y=True, label='Peso')
#
# ax1.legend(loc=1)
# ax1.ticklabel_format(style='plain', axis='y')
# ax1.set_ylabel('Valor')
# ax1.set_xlabel('Mes')
# ax2.legend(loc=2)
# ax2.ticklabel_format(style='plain', axis='y')
# ax2.set_ylabel('Peso')
#
# plt.grid('on', which='minor', axis='x')
# plt.grid('off', which='major', axis='x')
# plt.xlabel('Mes')
# plt.title('GLICERINA')
# plt.show()

# Agrupar valor por "Mes" - Grupo Fertilizante
# df['date'] = pd.to_datetime(df['Data emissão'])
# ax1 = df[df['Mercadoria grupo'] == 'FERTILIZANTE'].groupby([df['date'].dt.strftime('%m')])["Total do conhec."].agg('sum').plot(color='blue', grid=True, label='Valor', kind="bar")
# ax2 = df[df['Mercadoria grupo'] == 'FERTILIZANTE'].groupby([df['date'].dt.strftime('%m')])["Peso carregado"].agg('sum').plot(color='red', secondary_y=True, label='Peso')
#
# ax1.legend(loc=1)
# ax1.ticklabel_format(style='plain', axis='y')
# ax1.set_ylabel('Valor')
# ax1.set_xlabel('Mes')
# ax2.legend(loc=2)
# ax2.ticklabel_format(style='plain', axis='y')
# ax2.set_ylabel('Peso')
#
# plt.grid('on', which='minor', axis='x')
# plt.grid('off', which='major', axis='x')
# plt.xlabel('Mes')
# plt.title('FERTILIZANTE')
# plt.show()

# Agrupar valor por "Mes" - Grupo Oleos
# df['date'] = pd.to_datetime(df['Data emissão'])
# ax1 = df[df['Mercadoria grupo'] == 'OLEOS'].groupby([df['date'].dt.strftime('%m')])["Total do conhec."].agg('sum').plot(color='blue', grid=True, label='Valor', kind="bar")
# ax2 = df[df['Mercadoria grupo'] == 'OLEOS'].groupby([df['date'].dt.strftime('%m')])["Peso carregado"].agg('sum').plot(color='red', secondary_y=True, label='Peso')
#
# ax1.legend(loc=1)
# ax1.ticklabel_format(style='plain', axis='y')
# ax1.set_ylabel('Valor')
# ax1.set_xlabel('Mes')
# ax2.legend(loc=2)
# ax2.ticklabel_format(style='plain', axis='y')
# ax2.set_ylabel('Peso')
#
# plt.grid('on', which='minor', axis='x')
# plt.grid('off', which='major', axis='x')
# plt.xlabel('Mes')
# plt.title('OLEOS')
# plt.show()


# Agrupar valor por "Mes" - Grupo Algodão
# df['date'] = pd.to_datetime(df['Data emissão'])
# ax1 = df[df['Mercadoria grupo'] == 'ALGODÃO - COTTON'].groupby([df['date'].dt.strftime('%m')])["Total do conhec."].agg('sum').plot(color='blue', grid=True, label='Valor', kind="bar")
# ax2 = df[df['Mercadoria grupo'] == 'ALGODÃO - COTTON'].groupby([df['date'].dt.strftime('%m')])["Peso carregado"].agg('sum').plot(color='red', secondary_y=True, label='Peso')
#
# ax1.legend(loc=1)
# ax1.ticklabel_format(style='plain', axis='y')
# ax1.set_ylabel('Valor')
# ax1.set_xlabel('Mes')
# ax2.legend(loc=2)
# ax2.ticklabel_format(style='plain', axis='y')
# ax2.set_ylabel('Peso')
#
# plt.grid('on', which='minor', axis='x')
# plt.grid('off', which='major', axis='x')
# plt.xlabel('Mes')
# plt.title('ALGODÃO')
# plt.show()

# Agrupar valor por "Mes" - Grupo Outros
# df['date'] = pd.to_datetime(df['Data emissão'])
# ax1 = df[df['Mercadoria grupo'] == 'Outros'].groupby([df['date'].dt.strftime('%m')])["Total do conhec."].agg('sum').plot(color='blue', grid=True, label='Valor', kind="bar")
# ax2 = df[df['Mercadoria grupo'] == 'Outros'].groupby([df['date'].dt.strftime('%m')])["Peso carregado"].agg('sum').plot(color='red', secondary_y=True, label='Peso')
#
# ax1.legend(loc=1)
# ax1.ticklabel_format(style='plain', axis='y')
# ax1.set_ylabel('Valor')
# ax1.set_xlabel('Mes')
# ax2.legend(loc=2)
# ax2.ticklabel_format(style='plain', axis='y')
# ax2.set_ylabel('Peso')
#
# plt.grid('on', which='minor', axis='x')
# plt.grid('off', which='major', axis='x')
# plt.xlabel('Mes')
# plt.title('Outros')
# plt.show()

# Agrupar valor por "Mes" - Grupo Grãos
# df['date'] = pd.to_datetime(df['Data emissão'])
# ax1 = df[df['Mercadoria grupo'] == 'GRÃOS'].groupby([df['date'].dt.strftime('%m')])["Total do conhec."].agg('sum').plot(color='blue', grid=True, label='Valor', kind="bar")
# ax2 = df[df['Mercadoria grupo'] == 'GRÃOS'].groupby([df['date'].dt.strftime('%m')])["Peso carregado"].agg('sum').plot(color='red', secondary_y=True, label='Peso')
#
# ax1.legend(loc=1)
# ax1.ticklabel_format(style='plain', axis='y')
# ax1.set_ylabel('Valor')
# ax1.set_xlabel('Mes')
# ax2.legend(loc=2)
# ax2.ticklabel_format(style='plain', axis='y')
# ax2.set_ylabel('Peso')
#
# plt.grid('on', which='minor', axis='x')
# plt.grid('off', which='major', axis='x')
# plt.xlabel('Mes')
# plt.title('GRÃOS')
# plt.show()

# mapa de calor entre Mes/UF/Valor(R$)
# df['date'] = pd.to_datetime(df['Data emissão'])
# df1 = df.groupby([df['date'].dt.strftime('%m'), "UF da entrega"])["Total do conhec."].agg('sum').reset_index()
#
# piv = pd.pivot_table(df1, values='Total do conhec.', index=['date'], columns=['UF da entrega'], fill_value=0)
#
# formatter = tkr.ScalarFormatter(useMathText=True)
# formatter.set_scientific(False)
#
# sns.heatmap(piv, annot=True, cmap='Blues', fmt='.8g', cbar_kws={'format': formatter})
#
# plt.show()

# mapa de calor entre Mes/UF/Peso(kg)
# df['date'] = pd.to_datetime(df['Data emissão'])
# df1 = df.groupby([df['date'].dt.strftime('%m'), "UF da entrega"])["Peso carregado"].agg('sum').reset_index()
#
# piv = pd.pivot_table(df1, values='Peso carregado', index=['date'], columns=['UF da entrega'], fill_value=0)
#
# formatter = tkr.ScalarFormatter(useMathText=True)
# formatter.set_scientific(False)
#
# sns.heatmap(piv, annot=True, annot_kws={"size": 6}, cmap='Blues', fmt='.12g', cbar_kws={'format': formatter})
#
# plt.show()

# pedagio por grupo de mercadoria

# mapa de calor entre coleta x entrega x pedagio
# df1 = df.groupby(['UF da coleta', 'UF da entrega'])['Pedágio'].agg('sum').reset_index()
#
# piv = pd.pivot_table(df1, values='Pedágio', index=['UF da coleta'], columns=['UF da entrega'], fill_value=0)
#
# formatter = tkr.ScalarFormatter(useMathText=True)
# formatter.set_scientific(False)
#
# sns.heatmap(piv, annot=True, annot_kws={"size": 8}, cmap='Blues', fmt='.12g', cbar_kws={'format': formatter})
#
# plt.show()
