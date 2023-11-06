#!/usr/bin/env python3

import os, sys, subprocess
from subprocess import CalledProcessError

bin_path = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.dirname(bin_path)

START_CHDIR = f"cd {app_path}"
START_VENV = f". .env/bin/activate"
ADD_ENV_VARS = f'export APP_PATH={app_path} && export PYTHONDONTWRITEBYTECODE="true"'
STARTCOMMAND = f"python3 -B main.py"
COMMAND = START_CHDIR + " && " + ADD_ENV_VARS + " && "+ START_VENV + " && " + STARTCOMMAND

def main():
    try:
        subprocess.run(COMMAND, shell=True, check=True, stderr=subprocess.STDOUT)
    except (CalledProcessError, KeyboardInterrupt) as Err:
        print(Err)
    sys.exit()

if __name__ == "__main__":
    main()