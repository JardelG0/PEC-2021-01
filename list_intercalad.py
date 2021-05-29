def intercalado(A, B):
    intercal = []
    contador = 1
    for i in A:
        intercal.append(i)
    for j in B:
        intercal.insert(contador, j)
        contador += 2
    return intercal


def main():
    print('''---DIGITE 25 NÚMEROS PARA O GRUPO A E 25 PARA O GRUPO B---
OS ELEMENTOS SERÃO INTERCALADOS!''')
    lis_A = []
    lis_B = []
    for i in range(1, 25 + 1):
        A = int(input(f'Digite o {i}° do grupo A: '))
        lis_A.append(A)
    print("---Agora preencha o grupo B---")
    for j in range(1, 25 + 1):
        B = int(input(f'Digite o {j}° do grupo B: '))
        lis_B.append(B)

    print("Esse é o grupo A:", lis_A)
    print("E esse é o grupo B:",lis_B)
    print("Esses são os elementos do grupo A e B intercalados:",intercalado(lis_A, lis_B), end="")


if __name__ == "__main__":
    main()
