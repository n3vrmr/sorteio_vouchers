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
    Limpa o dataframe escolhido pelo argumento, tirando todas as linhas que não
    tenham 'Sucesso' na coluna 'Situação'.
    
    Argumentos
    -------
    df : objeto do tipo DataFrame.
    
    Returns
    -------
    planilha: objeto do tipo DataFrame apenas com as linhas que serão utilizadas 
    para fazer o sorteio.
    """
    planilha = df[df["Situação"] == "Sucesso"]
    return planilha

teste = limpar_planilha(teste)

def somar_valores(df):
    """
    Determina o valor total em reais das comprasa realizadas por cada pessoa, 
    retira as linhas com nomes duplicados, depois cria um novo DataFrame apenas
    com as informações necessárias para a realização do torneio: nome e o valor
    total.

    Parameters
    ----------
    df : objeto do tipo DataFrame.

    Returns
    -------
    para_uso : objeto do tipo DataFrame com duas colunas: 'Usuário' e 'Valor
    Pedido'.

    """
    users = []
    valor = []
    for nome in df["Usuário"]:
        tentativa = df[df["Usuário"] == nome]
        total = sum(tentativa["Valor Pedido"])
        tentativa = tentativa.drop_duplicates("Usuário")
        if nome not in users:
            users.append(tentativa["Usuário"].values[0])
            valor.append(total)
    para_uso = pd.DataFrame({"Usuário":users,
                             "Valor Pedido":valor})
    return para_uso
    
teste = somar_valores(teste)

def qtd_vouchers():
    """
    Calcula a quantidade de vouchers que cada pessoa tem baseado no valor gasto
    em reais. Uma pessoa recebe 1 (um) voucher a cada 10 (dez) reais gastos.
    Não existe pedido mínimo, então o mínimo de vouchers é 1.
    
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

qtd_vouchers()

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

arquivo_final = concatenar()

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

sorteio()

def main():
    t.sleep(5)
    print("Este foi o fim do sorteio. A JFH agradece a todos que participaram!")
    
if __name__ == '__main__':
    main()