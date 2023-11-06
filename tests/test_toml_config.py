from argparse import Namespace
from pydantic import BaseModel, ValidationError
from configs.toml_config import main, config_file_path_exists, import_toml, get_config

# -------------------- CHANGE THESE TO SUIT THE TEST CASE -------------------- #
good_file = Namespace(config_path="/home/jerry/Documents/GitRepos/toolsUI/tests/good.toml")
missing_file = Namespace(config_path="/home/jerry/Documents/GitRepos/toolsUI/tests/missing.toml")
corrupt_file = Namespace(config_path="/home/jerry/Documents/GitRepos/toolsUI/tests/corrupt.toml")
# ---------------------------------------------------------------------------- #

# -------------------------- TOML IMPORT VALIDATION -------------------------- #
class Key(BaseModel):
    value:str='test'
class Good(BaseModel):
    key: dict=Key
# ---------------------------------------------------------------------------- #

################################################################################
# --------------------------- INDIVIDUAL FUNCTIONS --------------------------- #
################################################################################
def test_config_path_exists_found():
    '''config_path + config_filename exists'''
    file_path = good_file.config_path
    isConfig, config_data = config_file_path_exists(file_path)
    assert type(isConfig) == bool; assert type(config_data) == str
    assert type(isConfig) != None; assert type(config_data) != None
    assert isConfig == True
# ---------------------------------------------------------------------------- #
def test_config_path_exists_not_found():
    '''config_path + config_filename does not exist'''
    file_path = missing_file.config_path
    isConfig, config_data = config_file_path_exists(file_path)
    assert type(isConfig) == bool; assert type(config_data) == str
    assert type(isConfig) != None; assert type(config_data) != None
    assert isConfig == False
# ---------------------------------------------------------------------------- #
def test_config_path_import_toml_good_file():
    '''config_path good, import good toml file.'''
    file_path = good_file.config_path
    isConfig, config_data = import_toml(file_path)
    assert type(isConfig) == bool; assert type(config_data) == dict
    assert type(isConfig) != None; assert type(config_data) != None
    assert isConfig == True
# ---------------------------------------------------------------------------- #
def test_config_path_import_toml_missing_file():
    '''config_path good, import missing toml file test'''
    file_path = missing_file.config_path
    isConfig, config_data = import_toml(file_path)
    assert type(isConfig) == bool; assert type(config_data) == str
    assert type(isConfig) != None; assert type(config_data) != None
    assert isConfig == False
# ---------------------------------------------------------------------------- #
def test_config_path_import_toml_corrupt_file():
    '''config_path good, import corrupt toml file test'''
    file_path = corrupt_file.config_path
    isConfig, config_data = import_toml(file_path)
    assert type(isConfig) == bool; assert type(config_data) == str
    assert type(isConfig) != None; assert type(config_data) != None
    assert isConfig == False
# ---------------------------------------------------------------------------- #
def test_toml_import_validation_good():
    '''config_path good, import good'''
    file_path = good_file.config_path
    isConfig, config_data = import_toml(file_path)
    assert type(isConfig) == bool; assert type(config_data) == dict
    assert type(isConfig) != None; assert type(config_data) != None
    assert isConfig == True
    assert config_data == {
        "key": {
            "value":"test"
        }
    }

################################################################################
# ------------------------------ FULL FUNCTIONS ------------------------------ #
################################################################################
def test_good_toml_main():
    '''Happy Path main function'''
    isConfig, config_data = main(good_file)
    assert type(isConfig) == bool; assert type(config_data) == dict
    assert type(isConfig) != None; assert type(config_data) != None
    assert isConfig == True
# ---------------------------------------------------------------------------- #
def test_missing_toml_main():
    '''config_path good, but toml file is missing'''
    isConfig, config_data = main(missing_file)
    assert type(isConfig) == bool; assert type(config_data) == str
    assert type(isConfig) != None; assert type(config_data) != None
    assert isConfig == False
# ---------------------------------------------------------------------------- #
def test_corrupt_toml_main():
    '''config_path good, but toml file is unparsable'''
    isConfig, config_data = main(corrupt_file)
    assert type(isConfig) == bool; assert type(config_data) == str
    assert type(isConfig) != None; assert type(config_data) != None
    assert isConfig == False

# EOF