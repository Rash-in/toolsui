import pytest, os
from main import get_env

@pytest.mark.asyncio
async def test_get_env_missing():
    '''Test missing file configs/toolsui.toml'''
    file_path = os.path.dirname(os.path.abspath(__file__)) + "/missing.toml"
    err_msg = await get_env(file_path)
    assert type(err_msg) == str
    assert err_msg == f"Config File does not exist: {file_path}"

@pytest.mark.asyncio
async def test_get_env_corrupt():
    file_path = os.path.dirname(os.path.abspath(__file__)) + "/corrupt.toml"
    err_msg = await get_env(file_path)
    assert type(err_msg) == str
    assert err_msg.startswith("Error importing config file")

@pytest.mark.asyncio
async def test_get_env_good():
    file_path = os.path.dirname(os.path.abspath(__file__)) + "/good.toml"
    err_msg = await get_env(file_path)
    assert err_msg is None
    assert os.environ['APP_PATH'] == "PLACEHOLDER"