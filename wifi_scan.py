import subprocess

ssid_base = open('ssid_base.txt', 'w')
signal_base = open('signal_base.txt', 'w')
sort_signal_base = open('sort_signal.txt', 'w')

def get_int():
	iw_out = subprocess.Popen(['iwconfig'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
	out_iw, err_iw = iw_out.communicate()

	for lines in out_iw.split('\n'):
		if "ESSID:" in lines:
			return lines.split('    ')[0]

def ssid():
	for lines in out.split('\t'):
		if 'SSID:' in lines:
			ssid = lines.split(' ', maxsplit=1)[1]
			ssid_base.write(ssid)
#			print(final)
	ssid_base.close()

def signal():		
	for lines in out.split('\t'):
		if 'signal:' in lines:
			signal = lines.split(' ', maxsplit=2)[1]
			signal_base.write(signal + '\n')
#			print(signal)
	signal_base.close()

interface = get_int()

process = subprocess.Popen(['iw', '%s' % interface , 'scan'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
out, err = process.communicate()

ssid()
signal()

ssid_base = open('ssid_base.txt', 'r')
signal_base = open('signal_base.txt', 'r')
list_ssid = ssid_base.readlines()
list_signal = signal_base.readlines()

base = dict(zip(list_ssid, list_signal))
base_d = list(base.items())
base_d.sort(key=lambda i: i[1])
for i in base_d:
	signal_dBm = float(i[1].rstrip())
	if signal_dBm <= 0.0 and signal_dBm >= -66.0:
		print("\033[32m {}".format(i[0].rstrip()), ':', "\033[32m {}".format(i[1].rstrip()))
	elif signal_dBm <= -67.0 and signal_dBm >= -88.0:
		print("\033[33m {}".format(i[0].rstrip()), ':', "\033[33m {}".format(i[1].rstrip()))
	elif signal_dBm <= -89.0:
		print("\033[31m {}".format(i[0].rstrip()), ':', "\033[31m {}".format(i[1].rstrip()))
