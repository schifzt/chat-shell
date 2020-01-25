#!python3
import subprocess
import shlex
import signal

# signal.SIGINT

def run_command(cmd):
    try:
        ps = subprocess.run(cmd, stdout=subprocess.PIPE, 
                            stderr=subprocess.STDOUT, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        return e.stdout
    else:
        return ps.stdout


def run_command_test(cmd):
    try:
        ps = subprocess.run(cmd, stdout=subprocess.PIPE, 
                            stderr=subprocess.STDOUT, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        return e.stdout.decode("utf-8")
    else:
        return ps.stdout.decode("utf-8")



if __name__ == "__main__":
    # cmd = "ls -l | grep md$"
    cmd = "cat test.py"
    # cmd = input()

    # cmd = shlex.quote(cmd)
    # cmd = shlex.split(cmd)
    # cmd = shlex.split(cmd[-1])

    out = run_command_test(cmd)
    print(out)


