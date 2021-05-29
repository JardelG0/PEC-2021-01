def mais_alto(name, alt):
    mais_alto = max(alt)
    print(f'JOGADOR MAIS ALTO DO TIME\n{name[alt.index(mais_alto)]}\n{mais_alto:.2f}')
    

def media(alt):
    return sum(alt) / len(alt)


def acima_media(name, alt):
    posicao = 0
    posica_ = []
    for i in alt:
        posicao += 1
        if i > media(alt):
            posica_.append(posicao - 1)

    print("JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME")
    for j in posica_:
        print(name[j])
        print(f'{alt[j]:.2f}')


def main():
    nomes = []
    alturas = []

    for i in range(12):
        name = str(input("Nome do Jogador: "))
        nomes.append(name)
        alt = float(input("Altura do rapaz: "))
        alturas.append(alt)
    
    mais_alto(nomes, alturas)
    print(f'ALTURA MÉDIA DO TIME\n{media(alturas):.2f}')
    acima_media(nomes, alturas)


if __name__ == "__main__":
    main()
