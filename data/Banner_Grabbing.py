import socket
def main():
			alvo = input("ALVO: ")
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect_ex((alvo, 22))
			print(sock.recv(2048))
			sock.close()