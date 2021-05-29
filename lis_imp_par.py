def par_impar(lista) : 
    par = []
    impar = []
    for j in lista:
        if j % 2 == 0:
            par.append(j)
        else:
            impar.append(j)
    return par, impar


def main():
    print("DIGITE 20 NÚMEROS PARA DIVIDÍ-LOS ENTRE ÍMPARES E PARES.")
    lis_ = []
    for i in range(1, 20 + 1):
        n = int(input(f'Digite o {i}° valor: '))
        lis_.append(n)
    par, impar = par_impar(lis_)

    print("Esses são os valores recebidos:", lis_)
    print("Esses são pares:", par)
    print("E esses são ímpares:", impar, end="")


if __name__ == "__main__":
    main()