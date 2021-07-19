import os
import sys
import socket
import platform
global R, B, C, Y, G, RT, CY, CO
CO='\033[m'
R='\033[1;31m'
B='\033[1;34m'
C='\033[1;37m'
CY='\033[1;36m'
Y='\033[1;33m'
G='\033[1;32m'
RT='\033[;0m'
def clear():
	os.system("cls" if os.name== "nt" else "clear")

def link():
	if platform.system() == "Windows":
		import webbrowser
		webbrowser.open_new_tab("https://chat.whatsapp.com/KOXdTEUngtTFrB47VoCnma")
	else:
		os.system("termux-open-url https://chat.whatsapp.com/KOXdTEUngtTFrB47VoCnma")

try:
	from data import autoback
	from data import portscan
	from data import Banner_Grabbing
	from data import Consulta_Whois
except Exception as error:
	print("ARQUIVO CORROMPIDO!" + str(error));exit()

def restart():
	python = sys.executable;os.excl(python, python, *sys.argv)

try:
	import whois
except:
	os.system("pip install whois");restart()

Sair = False
while(Sair == False):
	clear()
	print(f"""{C}
	[{Y}!{C}] Coded By {B}Kira Security{C} & {B}Kiny{C} in {Y}11/07/2021
	{R}Team Albania Security
	{C}|=============={G}MENU DE OPÇÕES{C}==============|
	| [ {G}1{C} ] Gerador de Backdoor                |
	| [ {G}2{C} ] Portscan                           |
	| [ {G}3{C} ] Banner Grabbing                    |
	| [ {G}4{C} ] Consulta Whois                     |
	| [ {G}5{C} ] Link da Team                       |
	| [ {G}6{C} ] Sair                               |
	|==========================================|
	""")

	op = int(input(f"[{Y}!{C}]{G} Digite a opção que deseja ~$ "))
	if op == 1:
		autoback.main()
	elif op == 2:
		portscan.main()
	elif op == 3:
		Banner_Grabbing.main()
	elif op == 4:
		Consulta_Whois.main()
	elif op == 5:
		link()
	elif op == 6:
		Sair = True

print("Adeus")
