import pyautogui
import webbrowser
from time import *

# Acessando o site e fazendo login
def login(usuario, senha):
    webbrowser.open_new('https://instagram.com')
    sleep(10)
    campo_login = pyautogui.locateCenterOnScreen('campo_login.png')
    
    if campo_login is not None:
        pyautogui.click(campo_login[0], campo_login[1], duration=1)
        pyautogui.typewrite(usuario)
        sleep(1)
        pyautogui.press('tab')
        sleep(1)
        pyautogui.typewrite(senha)
        sleep(1)
        pyautogui.press('enter')
    sleep(5)

def pesquisar(página):
    # localiza o centro da imagem pesquisar.png
    pesquisa = pyautogui.locateCenterOnScreen('pesquisar.png') 
    if pesquisa is not None:
        # Se a imagem existir, clica no centro dela
        pyautogui.click(pesquisa[0], pesquisa[1], duration=1)
    sleep(2)
    # Escreve o nome da página que o usuário passa
    pyautogui.typewrite(página)
    sleep(2)
    # Clica no primeiro resultado
    pyautogui.click(1321, 319, duration=1)


def like_comenta(comentário):
    sleep(2)
    try:
        # Ele tenta localizar a imagem coracao_marcado.png
        coracao_marcado = pyautogui.locateCenterOnScreen('coracao_marcado.png')
        # Se ele encontra o coração marcado, significa que o like já está marcado
        if coracao_marcado is not None:
            # Clica fora do post para sair dele
            pyautogui.click(1587,305, duration=1)
            # Aguarda 24 horas
            sleep(86400)
            # Pressiona F5 para recarregar a página e verificar se há um novo post
            pyautogui.press('f5')
        
    except pyautogui.ImageNotFoundException:
        # Se não encontrar o coração marcado, ele prossegue para dar like e comentar
        pyautogui.click(1449, 685, duration=1)
        sleep(2)
        pyautogui.move(40, 0, duration=1)
        pyautogui.click(duration=1)
        sleep(2)
        pyautogui.typewrite(comentário)
        sleep(2)
        pyautogui.press('enter')
        sleep(2)
        pyautogui.click(1587,305, duration=1)
        sleep(86400)
        pyautogui.press('f5')
        sleep(2)


usuario = ...
senha = ...

login(usuario, senha)

pesquisar('nike')
sleep(2)
pyautogui.scroll(-200)

while True:
    sleep(2)
    pyautogui.click(1268, 849, duration=1)
    sleep(2)
    comentario = 'Gostei do post!'
    like_comenta(comentario)