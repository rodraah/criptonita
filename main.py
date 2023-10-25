from sys import stdin, argv
from nicegui import ui

from rsa import criar_resposta

codigo = 0

def processar_resposta(x, y, z, cod):
  global resultado, chave_publica, chave_privada, codigo
  codigo = cod
  resposta = criar_resposta(x, y, z, codigo)
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

def limpar():
  global resultado, mensagem, chave_publica, chave_privada
  mensagem, chave_publica, chave_privada = "", "", ""
  resultado = "Digite algo para criptografar/descriptografar"

def botao_limpar():
  botao = ui.button('Limpar').classes('mx-auto').props('push')
  botao.on('click', lambda: limpar())

def area_resposta():
  global resultado
  with ui.card().style('width: 100%; height: 34%').props('push'):
    with ui.scroll_area():
      ui.html().bind_content(globals(), 'resultado')

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
  ui.run(port=porta)

# Se o usuário não enviar o texto pela linha de comando,
# esenha a interface
if stdin.isatty():
  # Porta para rodar o servidor local
  try:
    porta = int(argv[1])
  except:
    porta = 8080

  desenhar_interface()
# Se o usuário enviar o texto pela linha de comando:
else:
  mensagem = stdin.read()
  codigo = int(argv[1])
  print(f'codigo: {codigo}')
  try:
    chave_publica = argv[2]
    print(f'chave_publica: {chave_publica}')
    chave_privada = argv[3]
    print(f'chave_privada: {chave_privada}')
  except:
    chave_publica = None
    chave_privada = None
    codigo = 0
  print(criar_resposta(mensagem, chave_publica, chave_privada, codigo))

# vim: set shiftwidth=2 tabstop=2: