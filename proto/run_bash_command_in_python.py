#!python3

import subprocess

# cmd = "ls -l | cata"
cmd = input()

try:
	ps = subprocess.run(cmd, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell=True, check=True)
except subprocess.CalledProcessError as e:
	print(e.stdout.decode("utf-8"))
else:
	print(ps.stdout.decode("utf-8"))