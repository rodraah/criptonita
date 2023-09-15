from nicegui import ui

import string
import sys

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
      if i == " ":
        mensagem = mensagem + i
  return mensagem

def descriptografar (frase):
  mensagem = ""
  for i in frase:
    try: 
      mensagem  = mensagem + ALFABETO[CARACTERES.index(i)]
    except:
      if i == " ":
        mensagem = mensagem + i
  return mensagem

if not sys.stdin.isatty():
  user_input = sys.stdin.read()
  print(criptografar(user_input))
else:

  with ui.card().classes('mx-auto'):
    title = ui.label('Digite um texto').classes('mx-auto')
    user_input = ""
    ui.input().bind_value(globals(), 'user_input').classes('justify-center w-full')
    with ui.row():
      ui.button('Criptografar', on_click=lambda: resultado.set_text(f'Resultado: {criptografar(user_input)}')).props('push')
      ui.button('Descriptografar', on_click=lambda: resultado.set_text(f'Resultado: {descriptografar(user_input)}')).props('push')
    resultado = ui.label()
  ui.run()

# vim: set shiftwidth=2 tabstop=2:
