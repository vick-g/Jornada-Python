# bibliotecas = pacotes de codigo
# biblioteca --> *pyautogui*

import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5  # tempo de espera entre cada comando do pyautogui
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# comandos importantes do pyautogui
    # pyautogui.click() --> clicar com o mouse
    # pyautogui.write() --> escrever com o teclado
    # pyautogui.press() --> apertar uma tecla do teclado
    # pyautogui.hotkey() --> apertar uma combinação de teclas do teclado

# Passo a passo do programa
# Passo 1: Entrando no sistema da empresa
    # abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.hotkey("alt", "space")  # apertar alt + space para abrir o menu do chrome
pyautogui.press("x")  # apertar x para maximizar o chrome
time.sleep(1)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)  # esperar 3 segundos para o site abrir

# Passo 2: Fazer login
pyautogui.click(x=817, y=501)  # clicar no campo de email
pyautogui.write("victorgabrieldf2190@gmail.com")  # escrever o email
pyautogui.press("tab")  # ir para o campo de senha
pyautogui.write("senhaMaisDificilDoMundo")  # escrever a senha
pyautogui.press("tab")  # ir para o botão de login
pyautogui.press("enter")  # apertar o botão de login
pyautogui.press("enter")  # apertar o botão de login de novo após a verificação dos campos de email e senha

# Passo 3: Abrir a base de dados
tabela = pd.read_csv("aula-01-automacao-bots/produtos.csv", sep=";")  # ler a base de dados
# print(tabela)  # mostrar a tabela no terminal

for linha in tabela.index:
# Passo 4: Cadastrar 1 produto
    pyautogui.click(x=1150, y=369) # clicar em codigo do produto
# codigo
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab") # ir para o proximo campo
# marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab") 
# tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab") 
# categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab") 
# preco unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab") 
# custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(str(custo))
    pyautogui.press("tab") 
# obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":  # verificar se o campo de obs não está vazio
        pyautogui.write(obs)
    pyautogui.press("tab") 
    
    pyautogui.press("enter") # apertar o botão de enviar
    pyautogui.scroll(1000) # subir a tela para o proximo produto

# Passo 5: Repetir o passo 4 ate acabar a lista de produtos