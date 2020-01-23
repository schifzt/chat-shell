#!python3

import subprocess
import sys
import tty
import termios


def complete_command(word):
    '''Complete "word" by using Bash built-in command "compgen -c".
    Input:
        word to be completed
    Output:
        list of completions, or NoneType object
    '''
    cmd = "compgen -c " + word
    try:
        ps = subprocess.run(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(e.stdout.decode("utf-8"))
    else:
        return ps.stdout.splitlines()


def getch():
    '''Read one character.
    '''
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


CTRL_C = 3
BACK_SPACE = 127
ENTER = 13
TAB = 9

word = ""
select = 0
n_completions = 0
while True:
    key = ord(getch())
    if key == CTRL_C:
        break
    elif key == BACK_SPACE:
        word = word[:-1]
    else:
        select = 0
        word += chr(key)
        completions = complete_command(word)

    print(word)
    if not completions == None:
        print(list(map(lambda comp: comp.decode("utf-8"), completions))[:5])
