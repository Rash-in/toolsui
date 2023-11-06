#!/usr/bin/env python3

import os, sys, subprocess
from subprocess import CalledProcessError

bin_path = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.dirname(bin_path)

START_CHDIR = f"cd {app_path}"
START_VENV = f". .env/bin/activate"
ADD_ENV_VARS = f'export PYTHONDONTWRITEBYTECODE="true"'
STARTCOMMAND = f"pytest"

def start_tests():
    COMMAND = START_CHDIR + " && " + ADD_ENV_VARS + " && "+ START_VENV + " && " + STARTCOMMAND
    try:
        subprocess.run(COMMAND, shell=True, check=True, stderr=subprocess.STDOUT)
    except (CalledProcessError, KeyboardInterrupt) as Err:
        print(Err)
    return None

def remove_cache():
    REMOVE_CACHE = START_CHDIR + " && " + "rm -rf .pytest_cache"
    try:
        subprocess.run(REMOVE_CACHE, shell=True, check=True, stderr=subprocess.STDOUT)
    except (CalledProcessError, KeyboardInterrupt) as Err:
        print(Err)
    return None

def main():
    start_tests()
    remove_cache()

if __name__ == "__main__":
    main()