import random

def main():
    N = int(input())
    W = list(map(int, input().split())) 

    # N = 1000
    # W = [1] + random.sample(range(51, 1000000, 2), 999)

    ataques, restantes = jornada_nas_estrelas_v2(0, N, W, set(()))
    
    print(ataques, restantes, sep=" ")


def jornada_nas_estrelas(i: int, N: int, W: list, es_atacadas: set) -> None:

    if (i < 0) or (i >= N):
        return (len(es_atacadas), sum(W))

    ovelhas = W[i]

    if ovelhas > 0:
        W[i] = ovelhas - 1
        es_atacadas.add(i)

    i = proximo_movimento(ovelhas, i)
    return jornada_nas_estrelas(i, N, W, es_atacadas)


def jornada_nas_estrelas_v2(i: int, N: int, W: list, es_atacadas: set) -> None:
    
    while (i >= 0) and (i < N):
        
        ovelhas = W[i]

        if ovelhas > 0:
            W[i] = ovelhas - 1
            es_atacadas.add(i)

        i = proximo_movimento(ovelhas, i)
    
    return (len(es_atacadas), sum(W))


def jornada_nas_estrelas_v3(i: int, N: int, W: list, es_atacadas: set) -> None:
    """Fazer implementação usando vetores de True e False"""

def proximo_movimento(ovelhas: int, i) -> int:
    """Diz qual a próxima fazendo a ser visitada.

    x: número de ovelhas na fazenda
    i: indice da posição atual
    """

    if ovelhas % 2 == 0:
        return i - 1
    else:
        return i + 1


main()
