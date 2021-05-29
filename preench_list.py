def zero(posicoes):
    lis_ = []
    for i in range(posicoes):
        lis_.append(0)
    print("A quantia de '0' corresponde ao valor recebido:", lis_)


def sequenc_(posicoes):
    lis_ = []
    for i in range(1, posicoes + 1):
        lis_.append(i)
    print("A sequência corresponde ao valor recebido:", lis_)


def lis_input(qtd):
    lis_ = []
    for i in range(qtd):
        valores = int(input())
        lis_.append(valores)
    print("Esses são os valores que acabei de receber:", lis_)


def inverso(qtd):
    lis_ = []
    for i in range(qtd):
        vals = int(input())
        lis_.insert(0, vals)
    print("Esses são os valores recebidos na ordem invertida:", lis_, end="")


def main():
    n = int(input("Digite O valor a ser trabalhado: "))

    zero(n)
    sequenc_(n)
    lis_input(n)
    inverso(n)


if __name__ == "__main__":
    main()