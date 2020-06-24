import subprocess

process = subprocess.Popen(['iwconfig'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
out, err = process.communicate()

print(out)
