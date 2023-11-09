#!/usr/bin/env python3

import os, sys, argparse, subprocess
from subprocess import CalledProcessError

parser = argparse.ArgumentParser(
    prog="start_local",
    description="Starts local instance of toolsUI.",
    epilog="---"
)
parser.add_argument('-c', '--config_path', type=str, required=False, help="File path (path including file of where hypercorn.toml exists.)")
args = parser.parse_args()

bin_path = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.dirname(bin_path)

START_CHDIR = f"cd {app_path}"
START_VENV = f". .env/bin/activate"
ADD_ENV_VARS = f'export APP_PATH={app_path} && export PYTHONDONTWRITEBYTECODE="true"'
COMMAND = START_CHDIR + " && " + START_VENV + " && "+ ADD_ENV_VARS
def start_preconf():
    STARTCOMMAND_PRE = 'hypercorn --bind "0.0.0.0:5000" --worker-class "asyncio" --log-level "DEBUG" --error-logfile "-" --reload "main:toolsui"'
    all_command = COMMAND + " && " + STARTCOMMAND_PRE
    start_local(command=all_command)
    return None

def start_conf(file_path):
    STARTCOMMAND_CONF = f'hypercorn -c {file_path} "main:toolsui"'
    all_command = COMMAND + " && " + STARTCOMMAND_CONF
    start_local(command=all_command)
    return None

def start_local(command):
    try:
        subprocess.run(command, shell=True, check=True, stderr=subprocess.STDOUT)
    except (CalledProcessError, KeyboardInterrupt) as Err:
        print(Err)
    return None

def main(args):
    if not args.config_path:
        print("\nStarting preconfigured local instance.\n")
        start_preconf()
    else:
        if os.path.isfile(args.config_path):
            print(f"\nStarting local instance with config: {args.config_path}")
            start_conf(file_path=args.config_path)
    sys.exit()

if __name__ == "__main__":
    main(args)