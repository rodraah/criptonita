import string

CARACTERES = ['>', '_', 'q', ':', '²', 'T', '°', '6', '9', '@', '£', 'v', 'i', 
              '+', 'U', '§', '¹', 'R', '#', '=', '¢', '¬', '$', '7', '1', '&', 
              'b', 'º', 'G', '/', '8', '5', 'K', '*', '%', '!', ';', '0', ')', 
              '?', 'ç', '-', 'm', '2', ',', '.', '³', '<', 'ª', '3', '(', 'a']

ALFABETO = string.ascii_letters

def criptografar (frase):
  mensagem = ""
  for i in frase:
    try: 
      mensagem = mensagem + CARACTERES[ALFABETO.index(i)]
    except:
      if i == " " or i == "\n":
        mensagem = mensagem + i
      else: 
        print(f'ERRO: O caractere "{i}" não está no novo dicionário!')
  return mensagem

def descriptografar (frase):
  mensagem = ""
  for i in frase:
    try: 
      mensagem  = mensagem + ALFABETO[CARACTERES.index(i)]
    except:
      if i == " " or i == "\n":
        mensagem = mensagem + i
      else: 
        print(f'ERRO: O caractere "{i}" não está no novo dicionário!')
  return mensagem
