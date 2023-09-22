import sys
from nicegui import ui
# Importa o arquivo criptografia.py
import criptografia

def criar_resposta (mensagem, semente, codigo):
  # Se o código for 0, criptografa
  if codigo == 0:
    if semente != "":
      return criptografia.criptografar(mensagem, semente)
    else:
      return "Digite uma chave!!"
  # Se o código for 1, descriptografa
  elif codigo == 1:
    if semente != "":
      return criptografia.descriptografar(mensagem, semente)
    else:
      return "Digite uma chave!!"

# Se o usuário não enviar o texto pela linha de comando:
if sys.stdin.isatty():
  # Desenha a interface
  with ui.card().classes('mx-auto'):
    titulo = ui.label('CRIPTONITA').classes('mx-auto')
    mensagem = ""
    ui.input(label="Mensagem").bind_value(globals(), 'mensagem').classes('justify-center w-full')
    semente = ""
    ui.input(label="Chave").bind_value(globals(), 'semente').classes('justify-center w-full')
    with ui.row():
      ui.button('Criptografar', on_click=lambda: resultado.set_text(
        f'Resultado: {criar_resposta(mensagem, semente, 0)}')).props('push')
      ui.button('Descriptografar', on_click=lambda: resultado.set_text(
        f'Resultado: {criar_resposta(mensagem, semente, 1)}')).props('push')
    resultado = ui.label()
  ui.run()
# Se o usuário enviar o texto pela linha de comando:
else:
  mensagem = sys.stdin.read()
  semente = input("Digite sua chave: ")
  print(criptografia.criptografar(mensagem, semente))

# vim: set shiftwidth=2 tabstop=2: