from scapy.all import Dot11,Dot11Beacon,Dot11ProbeReq,Dot11Elt,RadioTap,sendp,hexdump

netSSID = 'MK_7'       #Network name here
iface = 'wlp5s0mon'         #Interface name here

dot11 = Dot11(type=0, subtype=4, addr1='2c:4d:54:1d:5f:00',
addr2='30:24:32:66:11:97', addr3='30:24:32:66:11:97')
probereq = Dot11ProbeReq()#(cap='ESS+privacy')
essid = Dot11Elt(ID='SSID',info=netSSID, len=len(netSSID))
dsset = Dot11Elt(ID='DSset', info='\x01')               #RSN Capabilities (no extra capabilities)

frame = RadioTap()/dot11/probereq/essid/dsset

frame.show()
print("\nHexdump of frame:")
hexdump(frame)
#raw_input("\nPress enter to start\n")

sendp(frame, iface=iface, inter=0.100, loop=1)
