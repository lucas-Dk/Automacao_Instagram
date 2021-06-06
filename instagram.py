# script de curtidas e comentários para o instagram            |
# criado por: lucas-Dk                                         | \
# esse script já tem uma conta própria então você                  by: lucas-Dk | Meu whatsapp: +5531986802198
# só precisa definir o usuário que irá receber os privilégios! | /
# fiz esse script para estudos!                                |

import os
import rich
import time
import sys
import pyautogui
from rich.console import Console
from selenium import webdriver
from time import sleep as esperar
from selenium.webdriver.common.keys import Keys

def limpar_terminal():
	if sys.platform == "win32":
		os.system("cls")
	elif sys.platform == "linux":
		os.system("clear")


console = Console()
limpar_terminal()
usuario_achar = str(input("[+] Informe o user para receber os privilégios: "))
console.print("\n[ 1 ] Ganhar curtidas",style="yellow bold")
console.print("[ 2 ] Ganhar comentários\n",style="yellow bold")
usar = str(input("[+] Qual privilégio você gostaria de obter: ")).strip()
if usar.isnumeric():
	usar = int(usar)
	if usar == 1:
		driver = webdriver.Chrome()
		driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
		esperar(2)
		try:
			pyautogui.click("tela.png")
		except:
			pyautogui.click("tela2.png")
		esperar(10)
		botao_login = driver.find_element_by_xpath("//input[@name='username']")
		botao_login.send_keys("walk_er_x")

		botao_senha = driver.find_element_by_xpath("//input[@name='password']")
		botao_senha.send_keys("senhaautomaticadowalker")
		botao_senha.send_keys(Keys.RETURN)
		esperar(5)
		limpar_terminal()
		fechar_informacoes = driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']")
		fechar_informacoes.send_keys(Keys.RETURN)
		esperar(8)

		fechar_notificacao = driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
		fechar_notificacao.send_keys(Keys.RETURN)
		esperar(5)

		pesquisar = driver.find_element_by_xpath("//div[@class='pbgfb Di7vw ']")
		pesquisar.click()

		driver.get("https://www.instagram.com/" + usuario_achar + "/")
		if sys.platform == "win32":
			os.system("cls")
		elif sys.platform == "linux":
			os.system("clear")
		esperar(4)
		for fotos in range(1, 100):
			esperar(2)
			fotos_user = driver.find_elements_by_xpath("//div[@class='_9AhH0']")
			for fotos in fotos_user:
				esperar(2)
				fotos.click()
				esperar(3)
				try:
					driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button").click()
				except:
					os.system("clear")
					console.print("[!] Desculpe, não consegui encontrar o botão de curtida... :(",style="red bold")
				else:
					console.print("[*] Curtida adicionada na foto do usuário "+usuario_achar+" !",style="green bold")
					fechar = driver.find_element_by_xpath("//div[@class='                     Igw0E     IwRSH      eGOV_         _4EzTm                                                                                  BI4qX            qJPeX            fm1AK   TxciK yiMZG']")
					esperar(2)
					fechar.click()
					esperar(1)
			console.print("As fotos acabaram! Fechando o programa!!")
			esperar(2)
			driver.quit()

	elif usar == 2:
		comentario_adicionar = str(input("[+] Comentário que deseja adicionar em todas as fotos: ")).strip()
		if usuario_achar:
			driver = webdriver.Chrome()
			driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
			esperar(2)
			pyautogui.click("tela.png")
			esperar(10)
			botao_login = driver.find_element_by_xpath("//input[@name='username']")
			botao_login.send_keys("walk_er_x")

			botao_senha = driver.find_element_by_xpath("//input[@name='password']")
			botao_senha.send_keys("senhaautomaticadowalker")
			botao_senha.send_keys(Keys.RETURN)
			esperar(10)

			fechar_informacoes = driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']")
			fechar_informacoes.send_keys(Keys.RETURN)
			esperar(8)

			fechar_notificacao = driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
			fechar_notificacao.send_keys(Keys.RETURN)
			esperar(5)

			pesquisar = driver.find_element_by_xpath("//div[@class='pbgfb Di7vw ']")
			pesquisar.click()

			driver.get("https://www.instagram.com/" + usuario_achar + "/")
			if sys.platform == "win32":
				os.system("cls")
			elif sys.platform == "linux":
				os.system("clear")
			esperar(4)
			for fotos in range(1, 100):
				esperar(2)
				fotos_user = driver.find_elements_by_xpath("//div[@class='_9AhH0']")
				for fotos in fotos_user:
					esperar(2)
					fotos.click()
					esperar(3)
					try:
						driver.find_element_by_class_name("Ypffh").click()
						comentar = driver.find_element_by_class_name("Ypffh")
						comentar.send_keys(comentario_adicionar)

					except:
						print("Não encontrei a barra para digitar!")
					else:
						esperar(2)
						comentar.send_keys(Keys.RETURN)
						fechar = driver.find_element_by_xpath("//div[@class='                     Igw0E     IwRSH      eGOV_         _4EzTm                                                                                  BI4qX            qJPeX            fm1AK   TxciK yiMZG']")
						esperar(2)
						fechar.click()
						esperar(1)
						console.print("[*] Comentário adicionado na foto do usuário " + usuario_achar + "!",style="green bold")
				print("\n[+] As fotos acabaram! Fechando o programa...")
				esperar(2)
				break
		driver.quit()

# Fim
