import socket
def main():
			alvo = input("ALVO: ")
			try:
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock.connect_ex((alvo, 22))
				print(sock.recv(2048))
				sock.close()
			except:
			  import time
			  print("Nenhuma info associada ao Host");time.sleep(3);pass
