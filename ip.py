print '''
##############################
# Verifica IP's              #
##############################
'''

#importando tools
import time, os, sys, getpass, linecache, subprocess

#listando user local
user = getpass.getuser()

## Abrindo, lendo e contando as linhas do  arquivo
look = open("ips.txt", "rw") 
print "Nome do arquivo:", look.name 
conta = subprocess.check_output(["wc", "-l", "ips.txt"])
print ("Numero de linhas: %s") %  conta 
look.close()

def contaip():
	while open(look)

#Cadastro de Ranges

netmask1 = ("192.168.0.0",24)
#netmask2 =
#netmask3 =
#netmask4 =
#netmask5 =
#netmask6 =

print ("Lista de Ranges Locaweb")
print netmask1






