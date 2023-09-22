import string
import random

# ALFABETO NORMAL COM TODOS OS CARACTERES (SEM ACENTOS),
# TODOS OS NÚMEROS E AS PONTUAÇÕES.
CARACTERES = []
for i in string.printable:
  CARACTERES.append(i)

# REMOVE ALGUNS CARACTERES PROBLEMÁTICOS
for i in ['\n', '\t', '\r', '\x0b', '\x0c']:
  CARACTERES.remove(i)

# VARIÁVEL QUE ARMAZENA A QUANTIDADE DE CARACTERES
QUANT_CARAC = len(CARACTERES)

# FUNÇÃO PARA CRIAR UM NOVO ALFABETO
# COM A SEMENTE DO USUÁRIO
def criar_alfabeto(semente):
  random.seed(int(semente))
  alfabeto = []

  while len(alfabeto) != QUANT_CARAC:
    numero = random.randint(0, (QUANT_CARAC - 1))
    caracter = CARACTERES[numero]
    if not caracter in alfabeto:
      alfabeto.append(caracter)

  return alfabeto

# FUNÇÃO PARA CRIPTOGRAFAR
def criptografar(frase, semente):
  novo_alfabeto = criar_alfabeto(semente)

  nova_frase = ""

  for i in frase:
    if i == "\n":
      nova_frase += "\n"
      continue
    #TODO! SOLUÇÃO TEMPORÁRIA PRA CARACTERES QUE NÃO TEM NA LISTA
    elif i not in CARACTERES:
      nova_frase += i
      continue
    nova_frase += novo_alfabeto[CARACTERES.index(i)]

  return nova_frase

# FUNÇÃO PARA DESCRIPTOGRAFAR
def descriptografar(frase, semente):
  novo_alfabeto = criar_alfabeto(semente)

  nova_frase = ""

  for i in frase:
    if i == "\n":
      nova_frase += "\n"
      continue
    #TODO! SOLUÇÃO TEMPORÁRIA PRA CARACTERES QUE NÃO TEM NA LISTA
    elif not i in CARACTERES:
      nova_frase += i
      continue
    nova_frase += CARACTERES[novo_alfabeto.index(i)]

  return nova_frase