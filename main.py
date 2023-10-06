import sys
from nicegui import ui

import rsa

# Se o usuário não enviar o texto pela linha de comando:
if sys.stdin.isatty():
  # Desenha a interface
  with ui.card().classes('mx-auto'):
    titulo = ui.label('CRIPTONITA').classes('mx-auto')
    mensagem = ""
    ui.input(label="Mensagem").bind_value(globals(), 'mensagem').classes('justify-center w-full')
    chave_publica = ""
    ui.input(label="Chave Pública").bind_value(globals(), 'chave_publica').classes('justify-center w-full')
    chave_privada = ""
    ui.input(label="Chave Privada").bind_value(globals(), 'chave_privada').classes('justify-center w-full')
    with ui.row().classes('mx-auto'):
      ui.button('Criptografar', on_click=lambda: resultado.set_text(
        f'Resultado: {rsa.criar_resposta(mensagem, chave_publica, chave_privada, 0)}')).props('push')
      ui.button('Descriptografar', on_click=lambda: resultado.set_text(
        f'Resultado: {rsa.criar_resposta(mensagem, chave_publica, chave_privada, 1)}')).props('push')
    resultado = ui.label()
  ui.run()
# Se o usuário enviar o texto pela linha de comando:
else:
  mensagem = sys.stdin.read()
  semente = sys.argv[1]
  try:
    codigo = int(sys.argv[2])
  except:
    codigo = 0
  print(criar_resposta(mensagem, semente, codigo))

# vim: set shiftwidth=2 tabstop=2: