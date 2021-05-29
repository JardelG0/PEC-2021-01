def comprimento(lista):
    contad = 0
    for i in lista:
        contad += 1
    print(f'Foram recebidos {contad} valores.')
    inverter(lista)


def inverter(lista):
    invertido = []
    for i in lista:
        invertido.insert(0, i)
    print(f'Sequência desses valores na forma inversa: {invertido}')
    minimo(lista)


def minimo(lista):
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    print(f'Menor valor recebido: {menor}')
    maximo(lista)
    

def maximo(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    print(f'Maior valor recebido: {maior}')
    soma(lista)


def soma(lista):
    soma_total = 0
    for i in lista:
        soma_total += i
    print(f'Soma dos valores recebidos: {soma_total}', end="")


def main():
    lis_ = []
    while True:
        valor = int(input("Digite o valor:"))
        if valor == 0: break
        lis_.append(valor)
    
    print(lis_)
    comprimento(lis_)


if __name__ == "__main__":
    main()
