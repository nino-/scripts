print '''
************************
	Brute Force
************************
'''

import time, os, sys, getpass, linecache, subprocess, socket, struct


def listauser():
	arquser = open_file('user.txt', 'r')


def listpassword():
	arqpass = open_file('password.txt', 'r')

host1 = raw_input("Whrite the HOST: ")

port = int(input(" 1 - FTP | 2 - SSH  "))

if port == 1:
	user = raw_input(" Deseja Digitar o usuairo? S|N")
		if user == 'n':
			print ("Pegando usuarios do arquivo %s" % arquser.name)


elif port == 2:
	user = raw_input(" Deseja Digitar o usuairo? S|N")
		if user == 'n':
			print ("Pegando usuarios do arquivo %s" % arquser.name)
