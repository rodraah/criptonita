import random
from math import gcd

# # RETORNA DOIS VALORES ALEATÓRIOS
# x = random.randint(1, 100)
# y = random.randint(1, 100)

# #FUNÇÃO PARA VALIDAR PRIMOS E GERA O "N"
# def dNums(x, y):
#     #VALIDAÇÃO DE PRIMOS: valor x
#     divisor, divisor1 = 0, 0
#     for cont in range(1, 100):
#         if x % cont == 0:
#             divisor += 1
#     if divisor <= 2:
#         print(x)
#     else:
#         return False
#     # VALIDAÇÃO DE PRIMOS: valor y
#     for cont1 in range(1, 100):
#         if y % cont1 == 0:
#             divisor1 += 1
#     if divisor1 <= 2:
#         print(y)
#     else:
#         return False
#     return x, y

# print(dNums(x, y))

# IGNOREI SEU SISTEMA DE VALIDAÇÃO DE NÚMEROS PRIMOS
# E ESCOLHI DOIS NÚMEROS PRIMOS
x = 13
y = 11

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
            kh = ord(i)
            kh = kh ** e
            kh = kh % n
            mensagem.append((kh))
        break

#MENSAGEM CRIPTOGRAFADA PUBLICA
print("MENSAGEM CRIPTOGRAFADA PUBLICA ", mensagem)

#Valor de D para descriptografar
# O VALOR DE D PRECISA ATENDER OS REQUISITOS:
# D * E % PHI = 1
d = 1
while (d * e % phi) != 1:
    d += 1

# print(d)

#DESCRIPTOGRAFAR A MENSAGEM
descriptografada = ""
for i in mensagem:
    i = i ** d
    i = i % n
    i = chr(i)
    descriptografada += i
print(f'MENSAGEM DESCRIPTOGRAFADA: "{descriptografada}"')