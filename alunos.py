def maior_d13(idade):
    list_posicao = []
    posicao = 0
    for i in idade:
        if i > 13:
            list_posicao.append(posicao)
        posicao += 1
    return list_posicao


def media(alt):
    return round(sum(alt) / len(alt), 2)


def alt_menor_media(posicao, alt, media):
    posicao_final = []
    for i in posicao:
        if alt[i] < media:
            posicao_final.append(i)
    return posicao_final


def main():
    nomes = []
    alturas = []
    idades = []

    for i in range(30):
        name = str(input("Nome do aluno: "))
        nomes.append(name)
        ano = int(input("Idade do aluno: "))
        idades.append(ano)
        alt = float(input("Altura do aluno: "))
        alturas.append(round(alt, 2))

    posicao_maior_d13 = maior_d13(idades)
    media_alt = media(alturas)
    posicao = alt_menor_media(posicao_maior_d13, alturas, media_alt)

    print("MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA")
    for j in posicao:
        print(nomes[j])


if __name__ == "__main__":
    main()
