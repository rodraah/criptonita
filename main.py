import sys
from nicegui import ui

import rsa

codigo = 0

def processar_resposta(x, y, z, cod):
  global resultado, chave_publica, chave_privada, codigo
  codigo = cod
  resposta = rsa.criar_resposta(x, y, z, codigo)
  if len(resposta) == 1:
    resultado = resposta[0]
    return None
  resultado, chave_publica, chave_privada = resposta[0], resposta[1], resposta[2]
  if codigo == 0:
    chave_descriptografar = resposta[3]
    resultado = f'''<p>Mensagem criptografada: <br>
      {resultado} <br>
      Chave para descriptografar: {chave_descriptografar}</p>'''
  if codigo == 1:
    resultado = f'''<p>Mensagem descriptografada: <br>
      {resultado}</p>'''

def botao_limpar():
  botao = ui.button('Limpar').classes('mx-auto').props('push')
  botao.on('click', lambda: desenhar_interface.refresh())

def area_resposta():
  global resultado
  with ui.card().style('width: 100%; height: 34%').props('push'):
    with ui.scroll_area():
      ui.html().bind_content(globals(), 'resultado')

@ui.refreshable
def desenhar_interface():
  global mensagem, chave_publica, chave_privada, resultado
  with ui.card().style('width: 450px; height: 500px; margin: auto'):
    titulo = ui.label('CRIPTONITA').classes('mx-auto')
    mensagem = ""
    ui.input(label="Mensagem").bind_value(globals(), 'mensagem').classes('justify-center w-full')
    chave_publica = ""
    ui.input(label="Chave Pública").bind_value(globals(), 'chave_publica').classes('justify-center w-full')
    chave_privada = ""
    ui.input(label="Chave Privada").bind_value(globals(), 'chave_privada').classes('justify-center w-full')
    with ui.row().classes('mx-auto'):
      ui.button('Criptografar', on_click=lambda: processar_resposta(mensagem, chave_publica, chave_privada, 0)).props('push')
      ui.button('Descriptografar', on_click=lambda: processar_resposta(mensagem, chave_publica, chave_privada, 1)).props('push')
      botao_limpar()
    resultado = f'Digite algo para criptografar/descriptografar'
    area_resposta()
    # ui.html().bind_content(globals(), 'resultado')
  ui.run()

# Se o usuário não enviar o texto pela linha de comando,
# esenha a interface
if sys.stdin.isatty():
  desenhar_interface()
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