#!python3
import subprocess
import shlex
import signal


# def send_SIGINT(signum, frame):
#     print("\nrun_commnad: SIGINT detected.")
#     p.send_signal(signal.SIGINT)


# def run_command(cmd):
#     try:
#         p = subprocess.run(cmd, stdout=subprocess.PIPE,
#                             stderr=subprocess.STDOUT, check=True, shell=True, timeout=3)
#     except subprocess.CalledProcessError as e:
#         return e.stdout
#     except subprocess.TimeoutExpired as e:
#         return b"time out"
#     else:
#         return p.stdout


def run_command(cmd, timeout=1):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT, shell=True)
    try:
        return p.communicate(timeout=timeout)[0]
    except subprocess.TimeoutExpired as e:
        return "Command \'{}\' timed out after {} seconds.\n".format(e.cmd, e.timeout).encode()


if __name__ == "__main__":
    # cmd = "ls -l | grep md$"
    cmd = "ls | lolcat"

    p1 = subprocess.Popen(cmd, stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE, 
                          shell=True)
    out = p1.communicate()
    print(out[0])
    print(out[1])
    print(out[0].decode("utf-8"))
