# criando um RPA
# Estou vivendo a minha melhor experiência de aprendizado




import yfinance
import pyperclip
import pyautogui
import time
import matplotlib.pyplot as plt

ticker = input("Digite o código da ação: ")
periodo = input("Digite o período desejado (ano:Y, mês: M, dia: D): ")
destinatario = input("Digite o destino de email que deseja enviar o relatório: ")
assunto_email = input("Digite o assunto do email: ")
dados = yfinance.Ticker(ticker)
tabela = dados.history(periodo)
fechamento = tabela.Close
grafico = fechamento.plot()
plt.savefig('Grafico.png')
maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento[-1]


mensagem = f"""
Olá, segue abaixo os dados da ação {ticker} no período de {periodo} :
Valor mais Alto :  R$ {round(maxima, 2)}
Valor mais Baixo : R$ {round(minima,2 )}
Valor Atual :      R$ {round(atual, 2)}
Gráfico da análise:
"""

pyautogui.Pause = 3
pyautogui.hotkey("ctrl", "t")
pyautogui.click(x=1758, y=147)
pyautogui.click(x=76, y=190)
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.press('tab')
pyperclip.copy(assunto_email)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.press('tab')
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.click(x=1433, y=1013)
pyperclip.copy(r"C:\Users\bielf\Jupyter\Projetos\Grafico")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.click(x=1325, y=1011)


print("tudo certo! ")