def soma_lists(A, B):
    c = []
    for i in range(20):
        soma = A[i] + B[i]
        c.append(soma)
    return c


def main():
    list_A = []
    list_B = []
    for i in range(40):
        if i < 20:
            A = int(input("Digite um valor para lista A: "))
            list_A.append(A)
        elif i >= 20:
            B = int(input("Digite um valor para lista B: "))
            list_B.append(B)
    
    print(f'Os valores da lista A são: {list_A}')
    print(f'Os valores da lista B são: {list_B}')
    print(f'A soma é: {soma_lists(list_A, list_B)}', end="")


if __name__ == "__main__":
    main()
