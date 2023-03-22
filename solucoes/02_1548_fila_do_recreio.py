def main():

    N = int(input())
    resultados = []

    for i in range(N):
        M = int(input())
        NOTAS = list(map(float, input().split()))
        NOTAS_ORDENADAS = sorted(NOTAS, reverse=True)
        alunos_reordenados = sum([(k != j) for k, j in zip(NOTAS, NOTAS_ORDENADAS)])
    
        resultados.append(M - alunos_reordenados)

    for i in resultados:
        print(i)
    

main()
