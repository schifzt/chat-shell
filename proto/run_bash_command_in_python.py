#!python3
import subprocess


def run_command(cmd):
    try:
        ps = subprocess.run(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        return e.stdout.decode("utf-8")
    else:
        return ps.stdout.decode("utf-8")


if __name__ == "__main__":
    cmd = "ls -l | grep ^tab"
    cmd = "read"
    # cmd = input()
    out = run_command(cmd)
    print(out)
