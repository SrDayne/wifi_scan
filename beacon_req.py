#!/usr/bin/env python
from scapy.all import *
 
interface = 'wlp5s0'
 
known={}
def callback(frame):
  if frame.haslayer(Dot11):
    if frame.haslayer(Dot11Beacon) or frame.haslayer(Dot11ProbeResp):
 
      source=frame[Dot11].addr2
      if source not in known:
        ssid = frame[Dot11Elt][0].info
        channel = frame[Dot11Elt][2].info
        channel = int(channel.encode('hex'), 16)
        print "SSID: '{}', BSSID: {}, channel: {}".format(ssid, source, channel)
        known[source]=True
 
sniff(iface=interface, prn=callback)
