def inverso(qtd):
    print(f'\nDIGITE {qtd} NÚMEROS.')
    lis_ = []
    for i in range(qtd):
        num = float(input("Digite Aqui: "))
        lis_.insert(0, num)
    print("Esses são os valores recebidos na ordem inversa",lis_)


def media_notas(qtd):
    print("\nVAMOS CALCULAR A SUA MÉDIA ESCOLAR.")
    if qtd == 0:
        print([])
        print("SEM NOTAS")
    else:
        notas = []
        for i in range(qtd):
            not_s = float(input("Digite a nota de um aluno: "))
            notas.append(not_s)
        media = sum(notas) / len(notas)
        print("Essas são as notas:",notas)
        print("Essa é a sua média:",round(media, 1))


def vog_cons(qtd):
    print("\nVAMOS BRINCAR COM AS LETRAS! :)")
    letras = []
    consoant = []
    vogais = 0
    for i in range(qtd):
        caracteres = str(input("Digite uma letra: "))[0]
        letras.append(caracteres)

    for i in letras:
        if i.upper() in "AEIOU":
            vogais += 1
        elif i.upper() in "BCDFGHJKLMNPQRSTVWXYZ":
            consoant.append(i)

    print(f'Foram digitadas {vogais} vogais.')
    print("E essas são as consoantes:",consoant, end="")
    print("Tchau Brigado... hehehe!! ;)")


def main():
    n = int(input("Com quantas posições iremos trabalhar? "))

    inverso(n)
    media_notas(n)
    vog_cons(n)


if __name__ == "__main__":
    main()