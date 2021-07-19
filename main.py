import os
import sys
import socket
import platform
def clear():
	os.system("cls");os.system("clear")

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

Sair = False
while(Sair == False):
	clear()
	print("""
	|==============MENU DE OPÇÕES==============|
	| [ 1 ] Gerador de Backdoor                |
	| [ 2 ] Portscan                           |
	| [ 3 ] Banner Grabbing                    |
	| [ 4 ] Consulta Whois                     |
	| [ 5 ] Link da Team                       |
	| [ 6 ] Sair                               |
	|==========================================|

	}-----{+} Coded By Kira Security & Kiny {+}-----{
	}-----{+}     11 July 2021       {+}-----{
	}-----{+} Team Albania Security  {+}-----{
	""")

	op = int(input("Digite a opção que deseja: "))
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