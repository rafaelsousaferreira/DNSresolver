#!/usr/bin/python

import socket,sys


if len(sys.argv) <1 :

	print "Modo de uso:<url>"
else :

	host = sys.argv[1]

	print host,"--->",socket.gethostbyname(host)



