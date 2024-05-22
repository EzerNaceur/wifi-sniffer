from scapy.all import *
import sys
interface = ''
probeReqs = []

def sniffProves(p):

	if p.haslayer(Dot11ProbeReq):
		netName = p.getlayer(Dot11ProbReq).info
		if netName not in probeReqs:
			probeReqs.append(netName)
			print('[+] Detected New Probe Request' + netName)

if __name__ == "__main__":
	if len(sys.argv) >= 2:
		interface = sys.argv[1]
		print('[+] Sniffing ' + interface + ' for any probe requests: \n')
		sniff(iface=interface, prn=sniffProves)
	else: 
		print("No interface provided. Provide an interface to start sniffing")
	
		

