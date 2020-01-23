#!python3

import subprocess
import pty

'''APPROACH 1
    Use `compgen` command.
'''
word = "gre"
completions = subprocess.check_output("compgen -c "+word, shell=True).splitlines()
print(list(map(lambda comp: comp.decode("utf-8"), completions)))


'''APPROACH 2
'''
