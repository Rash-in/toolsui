import os, argparse, tomllib, json
from typing import Union
from tomllib import TOMLDecodeError

config_file_name = "toolsui.toml"

parser = argparse.ArgumentParser(
    prog="toolsui.config.get_config",
    description="Config file validation",
    epilog="---"
)

parser.add_argument('-c', '--config_path', type=str, required=False, help="File path (including file of where the toml config file exists.)")
args = parser.parse_args()

def get_config(args) -> Union[bool, str|dict]:
    '''Procedures function to be imported in order to pull in toml config file'''
    config_path = args.config_path

    isFile, file_msg = config_file_path_exists(config_path)
    if not isFile:
        return isFile, file_msg
    
    return import_toml(config_path)

def import_toml(config_file) -> Union[bool,str|dict]:
    try:
        with open(config_file, "rb") as f:
            data = tomllib.load(f)
    except (TOMLDecodeError, FileNotFoundError) as Err:
        return False, f"Error importing config file: {config_file}\n   {Err}"
    else:
        return True, data

def config_file_path_exists(config_file_path) -> Union[bool, str]:
    success = os.path.isfile(config_file_path)
    if not success:
        msg = f"Config File does not exist: {config_file_path}"
    else:
        msg = f"Config File exists."
    print(f"---Checking if toolsui.toml exists in config_path\nSuccess? {success}\nMSG: {msg}\n")
    return success, msg

def main(args) -> Union[bool,str]:
    '''Used for validation and testing. Can be run as a file or in pytest.'''
    isConfig, config_data = get_config(args)
    print(json.dumps(config_data))
    return isConfig, config_data

if __name__ == "__main__":
    main(args)