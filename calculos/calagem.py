def calcular_calagem(v_atual, v_desejado, ctc, prnt):
    """
    Calcula a necessidade de calcário (t/ha).

    Fórmula:
    Necessidade = ((V2 - V1) * CTC) / (PRNT / 100)

    Parâmetros:
    v_atual (float): Valor atual de saturação por bases (V%) do solo.
    v_desejado (float): Valor desejado de saturação por bases (V%) do solo.
    ctc (float): Capacidade de troca de cátions (cmolc/dm³).
    prnt (float): Poder relativo de neutralização total do calcário (%).

    Retorna:
    float: Quantidade de calcário a ser aplicada (t/ha), arredondada para 2 casas decimais.
    """
    necessidade = ((v_desejado - v_atual) * ctc) / (prnt / 100)
    return round(necessidade, 2)