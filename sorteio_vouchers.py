# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 13:26:45 2022

@author: Nevermore
"""

import pandas as pd
import random as r
import time as t

def importar_arquivo(arquivo):
    """
    Importa um arquivo para ser lido pelo programa. O arquivo deve estar na
    mesma pasta que o programa no computador.
    Argumentos
    ----------
    arquivo : nome do arquivo em formato .xlsx a ser utilizado.
    Returns
    -------
    dataframe : objeto do tipo DataFrame.
    """
    dataframe = pd.read_excel(f"{arquivo}")
    return dataframe

# Altere o argumento entre aspas na linha abaixo para usar outro arquivo
teste = importar_arquivo('Relatório dos pedidos.xlsx')

def limpar_planilha(df):
    """
    Limpa o dataframe escolhido pelo argumento, tirando todas as linhas que tenham
    0 como valor na coluna 'Valor Pedido'.
    Returns
    -------
    planilha: objeto do tipo DataFrame apenas com as linhas que serão utilizadas 
    para fazer o sorteio.
    """
    planilha = df[df["Situação"] == "Sucesso"]
    return planilha

teste = limpar_planilha(teste)
users = []
valor = []
for nome in teste["Usuário"]:
    tentativa = teste[teste['Usuário'] == nome]
    total = sum(tentativa["Valor Pedido"])
    tentativa = tentativa.drop_duplicates("Usuário")
    users.append(tentativa["Usuário"].values[0])
    valor.append(total)
    
    

# def somar_valores(nome):
#     for elements in teste["Usuário"]:
#         if teste[teste["Usuário] == "Usuário"]:
#             total = sum(teste[])
#     return teste

# teste = somar_valores()

def qtd_vouchers():
    """
    Calcula a quantidade de vouchers que cada pessoa tem baseado no valor gasto
    em reais. Uma pessoa recebe 1 (um) voucher a cada 10 (dez) reais gastos.
    Returns
    -------
    teste : objeto do tipo DataFrame atualizado com uma nova coluna, que contém
    o número de vouchers de cada pessoa no DataFrame.
    """
    vouchers = []
    for items in teste['Valor Pedido']:
        x = int(items//10) + 1
        vouchers.append(x)
    teste['Vouchers'] = vouchers
    return teste

# qtd_vouchers()

def multiplicar_vouchers(nome):
    """
    Multiplica cada entrada no DataFrame pelo número de vouchers que a pessoa
    possui. Esta função existe apenas para ser usada dentro de outra função.
    Argumentos
    ----------
    nome : utiliza o nome das pessoas no DataFrame para poder multiplicar as
    entradas.
    Returns
    -------
    df_repeated : objeto do tipo DataFrame com entradas repetidas.
    """
    example = teste[teste['Usuário'] == f'{nome}']
    df_repeated = pd.concat([example]*example['Vouchers'].values[0], ignore_index=True, axis = 0)
    return df_repeated

def concatenar():
    """
    Cria uma lista e adiciona os vários DataFrames criados para cada pessoa no
    DataFrame inicial à lista. Depois, junta os DataFrames dessa lista em um.
    Returns
    -------
    done : objeto do tipo DataFrame contendo todas as entradas de acordo com o
    número de vouchers.
    """
    h = []
    for i in range(0,len(teste['Usuário'])):
        final = multiplicar_vouchers(teste['Usuário'].values[i])
        h.append(final)
        done = pd.concat(h, ignore_index=True)
    return done

# arquivo_final = concatenar()

def sorteio():
    """
    Sorteia uma pessoa do arquivo final aleatoriamente.
    Returns
    -------
    sorteado : nome da pessoa que ganhou o sorteio.
    """
    print("Sorteando...")
    t.sleep(1)
    print("10...")
    t.sleep(1)
    print("9...")
    t.sleep(1)
    print("8...")
    t.sleep(1)
    print("7...")
    t.sleep(1)
    print("6...")
    t.sleep(1)
    print("5...")
    t.sleep(1)
    print("4...")
    t.sleep(1)
    print("3...")
    t.sleep(1)
    print("2...")
    t.sleep(1)
    print("1...")
    t.sleep(1)
    print("0!")
    t.sleep(1)
    sorteado = arquivo_final['Usuário'][r.randint(0, len(arquivo_final['Usuário']))]
    text = f"Parabéns, {sorteado}, você acaba de ganhar o sorteio!"
    print(text)
    return sorteado

# sorteio()

def main():
    t.sleep(5)
    print("Este foi o fim do sorteio. A JFH agradece a todos que participaram!")
    
# if __name__ == '__main__':
#     main()