from biblioteca import *
while True:
    opr = str(input('Qual Operação Deseja Realizar?\n1 - SOMA\n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO\n0 - SAIR\nDIGITE AQUI:'))
    if opr == '0':
        break
    elif opr >='5':
        print("Número inválido escolha novamente")
    elif opr == '1'or'2'or'3'or'4':
        x = int(input("Digite um numero: "))
        y = int(input("Digite um numero: "))

        if opr == '1':
            soma(x,y)
        elif opr == '2':
            subtração(x,y)
        elif opr == '3':
            multiplicação(x,y)
        elif opr == '4':
            divisão(x,y)

print("Programa finalizado")