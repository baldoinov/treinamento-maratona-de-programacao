def main():
    
    A, B, C = sorted(map(float, input().split()), reverse=True)
    A2, B2, C2 = [x**2 for x in (A, B, C)]

    classificacoes = []

    if A >= (B + C):
        classificacoes.append("NAO FORMA TRIANGULO")
    else:
        if A2 == (B2 + C2):
            classificacoes.append("TRIANGULO RETANGULO")
        if A2 > (B2 + C2):
            classificacoes.append("TRIANGULO OBTUSANGULO")
        if A2 < (B2 + C2):
            classificacoes.append("TRIANGULO ACUTANGULO")
        if (A == B) and (B == C):
            classificacoes.append("TRIANGULO EQUILATERO")
        if ((A == B) and (A != C)) or ((A == C) and (A != B)) or ((B == C) and (A != B)):
            classificacoes.append("TRIANGULO ISOSCELES")

    print(*classificacoes, sep="\n")
    
main()
