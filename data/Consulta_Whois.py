import os, sys
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
			import whois
			dominio = input(f"{C}[{Y}!{C}] {G}Ip do Alvo ~/ ")
			try:
				consulta_whois = whois.whois(dominio)
				print(consulta_whois.text);time.sleep(5)
			except Exception as error:
				import time
				print(f"{R}ERRO! " + str(error));time.sleep(3)
				pass
