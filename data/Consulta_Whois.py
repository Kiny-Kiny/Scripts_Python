import socket
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
			alvo = input(f"{C}[{Y}!{C}] {G}Ip do Alvo ~/ ")
			try:
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock.connect_ex((alvo, 22))
				print(sock.recv(2048))
				sock.close()
			except:
			  import time
			  print(f"{R}Nenhuma info associada ao Host!");time.sleep(3);pass
