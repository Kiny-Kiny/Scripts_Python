import socket
import time
def main():
	host = input("Digite o alvo: ")
	portas = [80,8080,22,443,53,21,23]
	for porta in portas:
	       			meu_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	       			meu_socket.settimeout(0.1)
	       			codigo = meu_socket.connect_ex((host, porta))
	       			if codigo == 0:
	       				print("Porta",porta," está aberta");time.sleep(3)
	       			else:
	       				print("Porta",porta,"está  fechada");time.sleep(3)