import os

def main():
    print("-----Calculadora de média semestral!-----\n")

    cp1 = float(input("Insira a nota do primero Check Point (de 0 a 10): "))
    cp2 = float(input("Insira a nota do segundo Check Point (de 0 a 10): "))
    cp3 = float(input("Insira a nota do terceiro Check Point (de 0 a 10): "))
    sprint1 = float(input("Insira a nota da primeira sprint (de 0 a 10): "))
    sprint2 = float(input("Insira a nota da segunda sprint (de 0 a 10): "))
    gs = float(input("Insira a nota do Global Solution (de 0 a 10): "))


    if cp1 < 0 or cp1 > 10:
        os.system('cls')
        print('\nValor da CP1 inválido! (insira um número de 0 a 10)\n')
        main()
    if cp2 < 0 or cp2 > 10:
        os.system('cls')
        print('\nValor da CP2 inválido! (insira um número de 0 a 10)\n')
        main()
        os.system('cls')
    if cp3 < 0 or cp3 > 10:
        os.system('cls')
        print('\nValor da CP3 inválido! (insira um número de 0 a 10)\n')
        main()
    if sprint1 < 0 or sprint1 > 10:
        os.system('cls')
        print('\nValor da Sprint 1 inválido! (insira um número de 0 a 10)\n')
        main()
    if sprint2 < 0 or sprint2 > 10:
        os.system('cls')
        print('\nValor da Sprint 2 inválido! (insira um número de 0 a 10)\n')
        main()
    if gs < 0 or gs > 10:
        os.system('cls')
        print('\nValor da Global Solution inválido! (insira um número de 0 a 10)\n')
        main()

    menor_cp = 1

    if cp1 < cp2 and cp1 < cp3:
        cp1 = menor_cp
    if cp2 < cp3 and cp2 < cp1:
        cp2 = menor_cp
    if cp3 < cp1 and cp3 < cp2:
        cp3 = menor_cp
    if cp1 == cp2 and cp2 == cp3:
        menor_cp = cp1

    media = (cp1 + cp2 + cp3 - menor_cp + sprint1 + sprint2)/4 * 0.4 + (gs *0.6)
    media_peso = media * 0.4

    print(f'A média semestral sem o peso é: {media:.1f}!')
    print(f'A média semestral com peso é: {media_peso:.1f}! (o peso do primeiro semestre é de 40%)')

if __name__ == '__main__':
    main()