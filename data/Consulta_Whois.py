import os, sys
def main():
			try:
				import whois
			except:
				os.system("pip install whois")
				import whois
			dominio = input("IP ALVO: ")
			consulta_whois = whois.whois(dominio)
			try:
				print(consulta_whois.text);time.sleep(5)
			except:
				pass
