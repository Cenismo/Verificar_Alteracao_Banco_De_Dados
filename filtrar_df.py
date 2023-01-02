import pandas as pd
from filtrar_df import *

# Carregue os dados das duas abas em dataframes do Pandas
query_result = pd.read_excel('teste.xlsx', sheet_name='queryResult')
anterior = pd.read_excel('teste.xlsx', sheet_name='anterior')

# Obtenha os id_rules que existem apenas na aba "queryResult"
result = query_result[~query_result['rule_id'].isin(anterior['rule_id'])]

# Adicione uma coluna "origem" ao dataframe result
result = result.copy()
result['origem'] = 'queryResult'

# Obtenha os id_rules que existem apenas na aba "anterior"
result_inv = anterior[~anterior['rule_id'].isin(query_result['rule_id'])]

# Adicione uma coluna "origem" ao dataframe result_inv
result_inv = result_inv.copy()
result_inv['origem'] = 'anterior'


# Concatene os dataframes result e result_inv em um único dataframe
result_final = pd.concat([result, result_inv])

# Salve o dataframe "result_final" em uma nova aba chamada "alerta_rules" no arquivo do Google Sheets
result_final.to_excel('final.xlsx', index=False, sheet_name='alerta_rules_filtro')

#Crie um dataframe vazio
filtered_result = pd.DataFrame(columns=result_final.columns)

#Crie um dataframe vazio
filtered_result = pd.DataFrame(columns=result_final.columns)

#Percorra todas as linhas do dataframe "result_final"
for index, row in result_final.iterrows():
    # Verifique o valor da coluna "origem"
    if row['origem'] == 'anterior':
            # Verifique se o "rules" e o "id_parceiro" não existem na aba "queryResult"
        if query_result[(query_result['rules'] == row['rules']) & (query_result['id_parceiro'] == row['id_parceiro'])].empty:
            # Adicione a linha ao dataframe "filtered_result"
            filtered_result = pd.concat([filtered_result, row.to_frame().T])
    else:
                # Verifique se o "rules" e o "id_parceiro" não existem na aba "anterior"

        if anterior[(anterior['rules'] == row['rules']) & (anterior['id_parceiro'] == row['id_parceiro'])].empty:
            # Adicione a linha ao dataframe "filtered_result"
            filtered_result = pd.concat([filtered_result, row.to_frame().T])

            #Salve o dataframe "filtered_result"
filtered_result.to_excel('final.xlsx', index=False, sheet_name='alerta_rules_filtro')

