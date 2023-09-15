from nicegui import ui

import criptografia

import sys

# Se o usuário não enviar o texto pela linha de comando:
if sys.stdin.isatty():
  # Desenha a interface
  with ui.card().classes('mx-auto'):
    title = ui.label('Digite um texto').classes('mx-auto')
    user_input = ""
    ui.input().bind_value(globals(), 'user_input').classes('justify-center w-full')
    with ui.row():
      ui.button('Criptografar', on_click=lambda: resultado.set_text(
        f'Resultado: {criptografia.criptografar(user_input)}')).props('push')
      ui.button('Descriptografar', on_click=lambda: resultado.set_text(
        f'Resultado: {criptografia.descriptografar(user_input)}')).props('push')
    resultado = ui.label()
  ui.run()
# Se o usuário enviar o texto pela linha de comando:
else:
  user_input = sys.stdin.read()
  print(criptografia.criptografar(user_input))

# vim: set shiftwidth=2 tabstop=2:
