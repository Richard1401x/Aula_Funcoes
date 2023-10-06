

def soma (n1,n2):
    resultado = n1+n2
    print(f'RESULTADO\n {resultado}')

def subtração (n1,n2):
    resultado = n1-n2
    print(f'RESULTADO\n {resultado}')

def multiplicação (n1,n2):
    resultado = n1*n2
    print(f'RESULTADO\n {resultado}')

def divisão (n1,n2):
    resultado = n1/n2
    print(f'RESULTADO\n {resultado}')

def pir (n):
    for x in range(n+1):
         print (str(x)*x)

def vogais (v1):
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    for v in v1:
        if v == 'a':
            cont1 += 1
        elif v == 'e':
            cont2 += 1
        elif v == 'i':
            cont3 += 1
        elif v == 'o':
            cont4 += 1
        elif v == 'u':
            cont5 += 1

    print(f'Vogais [a] tem: {cont1}\nVogais [e] tem: {cont2}\nVogais [i] tem: {cont3}\nVogais [o] tem: {cont4}\nVogais [u] tem: {cont5}')
