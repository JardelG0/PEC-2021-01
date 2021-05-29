def count(lista, pesq):
    ocorrenc_ = 0
    for i in lista:
        if i == pesq:
            ocorrenc_ += 1
    return ocorrenc_


def main():
    list_ = []
    while True:
        valor_list = int(input("Digite um valor: "))
        if valor_list == 0: break
        list_.append(valor_list)
    valor_pesq = int(input("Qual o valor que você quer buscar? "))

    print(f'Esses são os valores recebidos: {list_}\nO valor a ser buscado é {valor_pesq}.')
    print(f'Após realizar a busca o valor {valor_pesq} aparece {count(list_, valor_pesq)} vezes.', end="")


if __name__ == "__main__":
    main()
