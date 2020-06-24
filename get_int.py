import subprocess

def get_int():
	iw_out = subprocess.Popen(['iwconfig'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
	out_iw, err_iw = iw_out.communicate()

	for lines in out_iw.split('\n'):
		if "ESSID:" in lines:
			return lines.split('    ')[0]
			
print(get_int())
