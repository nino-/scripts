#!/sbin/python

print '''
##############################
Copiando comandos para bashrc
##############################
'''
import os, subprocess, sys

home = "/home/nino/.bashrc"

abrir = open("/home/nino/.bashrc", "r")
for line in abrir:
	if 'ifconfig' in line:
		roda = os.system("source %s" % home)
		print(" ALIAS OK")
		break

else:
	copia = os.system("echo 'alias ifconfig=/sbin/./ifconfig' >> /home/nino/.bashrc")
	roda = os.system("source /home/nino/.bashrc")
	print("Inclsuo Alias e Source")

	



