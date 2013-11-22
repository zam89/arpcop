import sys,subprocess

if len(sys.argv)!=2:
	print "syntax: "+sys.argv[0]+"\n"
	exit()
ettercap=subprocess.Popen("ettercap -i "+sys.argv[1]+" -TQP arp_cop //",
shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
try:
	while 1:
		inPut=ettercap.stdout.readline()
		inPut=inPut.split(" ")
		for msg in inPut:
			if msg=="(WARNING)":
				print "ARP Poisoning Detected"
except:
	print "Terminated"
