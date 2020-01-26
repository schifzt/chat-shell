#!python3
import subprocess
import sys
import tty
import termios


# def complete_command(word):
#     '''Complete "word" by using Bash built-in command "compgen -c".
#     Input:
#         word to be completed
#     Output:
#         list of completions, or NoneType object
#     '''
#     cmd = "compgen -c " + word
#     try:
#         p = subprocess.run(cmd, stdout=subprocess.PIPE,
#                             stderr=subprocess.STDOUT, shell=True, check=True)
#     except subprocess.CalledProcessError as e:
#         # return e.stdout
#         return b"error !\n"
#     else:
#         return p.stdout.splitlines()


def complete_command(word):
    '''Complete "word" by using Bash built-in command "compgen -c".
    Input:
        word to be completed
    Output:
        list of completions, or b"" if completions is None
    '''
    cmd = "compgen -c " + word
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT, shell=True)
    out = p.communicate()[0]
    return b"" if out == None else out 



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


if __name__ == "__main__":
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
            print((completions.decode("utf-8"))+"\n")
    