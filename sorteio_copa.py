# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 15:47:57 2022

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

planilha = importar_arquivo("Relatório dos pedidos.xlsx")

def limpar_planilha(df):
    """
    Limpa o dataframe escolhido pelo argumento, tirando todas as linhas que não
    tenham 'Sucesso' na coluna 'Situação'.
    
    Argumentos
    -------
    df : objeto do tipo DataFrame.
    
    Returns
    -------
    planilha: objeto do tipo DataFrame apenas com as linhas que serão
    utilizadas para fazer o sorteio.
    """
    planilha_limpa = df[df["Situação"] == "Sucesso"]
    return planilha_limpa

planilha_sucesso = limpar_planilha(planilha)

def compras_acima(df,valor:int):
    """
    Limpa o DataFrame escolhido para selecionar apenas compras acima de um
    certo valor.

    Parameters
    ----------
    df : objeto do tipo DataFrame.
    
    valor : valor mínimo do pedido para que a pessoa participe do sorteio.

    Returns
    -------
    planilha_valores : objeto do tipo DataFrame apenas com as compras acima do
    valor escolhido.

    """
    planilha_valores = df[df["Valor Pedido"] >= valor]
    return planilha_valores

planilha_compras = compras_acima(planilha_sucesso, 15)

def qtd_vouchers(df):
    """
    Determina a quantidade de vouchers de cada pessoa, depois cria um novo
    DataFrame apenas com as colunas necessárias para a realização do sorteio.

    Parameters
    ----------
    df : objeto do tipo DataFrame.

    Returns
    -------
    para_uso : objeto do tipo DataFrame com duas colunas: 'Usuário' e
    'Vouchers'.
    
    """
    contagem_nomes = df["Usuário"].value_counts()
    users = list(contagem_nomes.index)
    vouchers = list(contagem_nomes.values)
    novo_df = pd.DataFrame({"Usuário":users,
                            "Vouchers":vouchers})
    return novo_df

planilha_vouchers = qtd_vouchers(planilha_compras)

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
    individuais = planilha_vouchers[planilha_vouchers["Usuário"] == f"{nome}"]
    df_repeated = pd.concat([individuais]*individuais["Vouchers"].values[0],
                            ignore_index=True, axis = 0)
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
    for i in range(0,len(planilha_vouchers["Usuário"])):
        final = multiplicar_vouchers(planilha_vouchers["Usuário"].values[i])
        h.append(final)
        done = pd.concat(h, ignore_index=True)
    return done

planilha_final = concatenar()

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
    sorteado = planilha_final["Usuário"][r.randint(0,
                                         len(planilha_final['Usuário'])-1)]
    text = f"Parabéns, {sorteado}, você acaba de marcar um golaço com a JFH!"
    print(text)
    return sorteado

sorteio()

def main():
    t.sleep(5)
    print("Este foi o fim do sorteio. Vamos juntos rumo ao HEXA!")
    
if __name__ == '__main__':
    main()
