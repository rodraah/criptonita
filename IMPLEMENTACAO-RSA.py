import random
from math import gcd, pow

# RETORNA DOIS VALORES ALEATÓRIOS
x = random.randint(1, 100)
y = random.randint(1, 100)

#FUNÇÃO PARA VALIDAR PRIMOS E GERA O "N"
def dNums(x, y):
    #VALIDAÇÃO DE PRIMOS: valor x
    divisor, divisor1 = 0, 0
    for cont in range(1, 100):
        if x % cont == 0:
            divisor += 1
    if divisor <= 2:
        print(x)
    else:
        return False
    # VALIDAÇÃO DE PRIMOS: valor y
    for cont1 in range(1, 100):
        if y % cont1 == 0:
            divisor1 += 1
    if divisor1 <= 2:
        print(y)
    else:
        return False
    return x, y

print(dNums(x, y))

#VALOR DE "N"
n = x * y

#VALOR DE PHI(N)
phi = (x-1)*(y-1)

#CHAVE PUBLICA COMPOSTA PELO N E E
mensagem = []
while True:
    e = random.randint(1, 100)
    if e > 1 and e < phi and gcd(phi, e) == 1:
        digite = input("Digite algo: ")
        for i in digite:
            kh = pow(ord(i), e)
            kh = kh % n
            mensagem.append((kh))
        break

#MENSAGEM CRIPTOGRAFADA PUBLICA
print("MENSAGEM CRIPTOGRAFADA PUBLICA ", mensagem)

#Valor de D para descriptografar
d = e % phi

#DESCRIPTOGRAFAR A MENSAGEM
lista = []
for i in mensagem:
    result = i ** d
    texto = int(result % n)
    letra = chr(texto)
    lista.append(letra)
    i += 1
print("EM TESE, MENSAGEM DESCRIPTOGRAFADA", lista)