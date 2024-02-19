import pyautogui as posicaoAbreArquivos

posicaoAbreArquivos.hotkey('win','r')

posicaoAbreArquivos.typewrite('notepad')

posicaoAbreArquivos.press('enter')

posicaoAbreArquivos.sleep(3)

posicaoAbreArquivos.typewrite('entrei atraves de codigo')

posicaoAbreArquivos.sleep(2)

fecharJanelaNotepad = posicaoAbreArquivos.getActiveWindow()

posicaoAbreArquivos.sleep(2)

fecharJanelaNotepad.close()

posicaoAbreArquivos.sleep(2)

posicaoAbreArquivos.press('tab')

posicaoAbreArquivos.sleep(2)

posicaoAbreArquivos.press('enter')


"""
Criando menu de opções para abrir o excel, word ou notepad
"""

import pyautogui
import pyautogui as escolha_opcao

opcao = pyautogui.confirm('clique no botão desejado', buttons = ['Excel', 'Word', 'Notepad'])

if opcao == 'Excel':
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('Excel')
    escolha_opcao.press('Enter')
    escolha_opcao.sleep(6)
    escolha_opcao.click(x=434, y=273)
    escolha_opcao.sleep(3)
    escolha_opcao.typewrite('Escolhi abrir o Excel')
elif opcao == 'Word':
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('winword')
    escolha_opcao.press('Enter')
    escolha_opcao.sleep(6)
    escolha_opcao.click(x=449, y=309)
    escolha_opcao.sleep(3)
    escolha_opcao.typewrite('Escolhi abrir o Word')
elif opcao == 'Notepad':
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('notepad')
    escolha_opcao.press('Enter')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('Escolhi abrir o Notepad')