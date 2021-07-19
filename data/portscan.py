import socket
import time
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
	host = input(f"{C}[{Y}!{C}] {G}Digite o {Y}IP{G} alvo ~/ ")
	portas = [80,8080,22,443,53,21,23]
	for porta in portas:
	       			try:
	       				meu_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	       				meu_socket.settimeout(0.1)
	       				codigo = meu_socket.connect_ex((host, porta))
	       				if codigo == 0:
	       					print(f"{G}Porta",porta," está aberta");time.sleep(3);pass
	       				else:
	       					print(f"{G}Porta",porta,"está  fechada");time.sleep(3);pass
	       			except Exception as error:
	       				print(f'{R}Nenhuma info associada ao Host: ' + str(error));time.sleep(2);pass
