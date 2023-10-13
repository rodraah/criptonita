import random
import time

def é_primo(num):
  '''
  Retorna verdadeiro se o número for primo
  e falso se não for
  '''
  num = int(num)
  divisores = 0
  for i in range(1,num):
    if num % i == 0:
      divisores += 1
    if divisores > 1:
      break
  if divisores == 1:
    return True
  else:
    return False

def mdc(x,y):
  '''
  Retorna o máximo divisor comum entre x e y
  '''
  x = listar_divisores(x)
  y = listar_divisores(y)
  divisor = []
  for i in x:
    if i in y and i not in divisor:
      divisor.append(i)
  for i in y:
    if i in x and i not in divisor:
      divisor.append(i)
  divisor = divisor[len(divisor)-1]
  return divisor

def listar_divisores(x):
  '''
  Lista os divisores de x
  '''
  lista = []
  for i in range(1,x):
    if x % i == 0:
      lista.append(i)
  lista.append(x)
  return lista

def gera_num_aleatorio():
  '''
  Gera um número aleatório
  '''
  return random.randint(100,1000)

def criar_chaves(mensagem):
  # Gera P e Q
  # O P SERÁ A QUANTIDADE DE CARACTERES
  # ELEVADO A 2
  p = len(mensagem) ** 2

  # O Q SERÁ A DATA ATUAL MOD 10
  # ELEVADO A 5
  q = int(time.time()) % 100

  # E força eles a serem primos
  while True:
    if not é_primo(p):
      p += 1
    if not é_primo(q):
      q += 1
    if é_primo(p) and é_primo(q):
      break

  # N = P * Q
  n = p * q

  # Calculo de phi
  phi = (p-1) * (q-1)

  # "E" é um número aleatório que
  # preenche os requisitos abaixo
  e = gera_num_aleatorio()
  while True:
    a = mdc(phi, e)
    if e > 1 and phi > e and é_primo(e):
      if a == 1:
        break
    e += 1
  
  return n,e,phi

def criar_resposta(x, publica, privada, codigo):
  # Se o código for 0, criptografa
  if codigo == 0:
    # Mensagem:
    mensagem = []
    for i in x:
      i = ord(i)
      mensagem.append(i)

    # Se o usuário não digitar as chaves, gera elas
    if not publica:
      n,e,phi = criar_chaves(mensagem)
    else:
      n = int(publica)
      e = int(privada)

    # Criptografar
    mensagem_criptografada = []
    for i in mensagem:
      i = i ** e
      i = i % n
      mensagem_criptografada.append(i)

    print(f'Mensagem criptografada: {mensagem_criptografada}')
    # Chave privada para descriptografar
    try: 
      d = 1
      while (d * e % phi) != 1:
        d += 1
    except:
      d = ""
    
    # Chave pública é o N e o E
    print(f'Sua chave pública é: "{n}" e "{e}"')
    return [mensagem_criptografada, n, e, d]

  # Se o código for 1, descriptografa
  elif codigo == 1:

    if not privada:
      # Chave privada (D)
      return "Digite uma chave privada!!"
    else:
      n = int(publica)
      d = int(privada)

    # Tranforma a mensagem em uma lista válida
    try: 
      mensagem = f'{x}'.replace('[', '').replace(']', '')
      mensagem = list(mensagem.split(', '))
      for i in range(0, len(mensagem)):
        mensagem[i] = int(mensagem[i])
    except:
      mensagem = "Erro ao descriptografar. Verifique sua chave e sua mensagem."
      print(mensagem)
      return [mensagem]

    print(mensagem)

    # Descriptografar
    mensagem_descriptografada = ""
    for i in mensagem:
      i = i ** d
      i = i % n
      i = chr(i)
      mensagem_descriptografada += i

    print(f'Mensagem descriptografada: {mensagem_descriptografada}')
    return [mensagem_descriptografada, n, d, None]

  else:
    return f'{codigo} não é um código válido!!'
