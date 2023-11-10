import os, time, asyncio, tomllib
from tomllib import TOMLDecodeError
from hypercorn.asyncio import serve
from hypercorn import Config
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from routes import default_routers

app_path = os.path.dirname(os.path.abspath(__file__))
hypercorn_config_path = app_path + "/configs/hypercorn.toml"
config = Config()

async def get_env(config_path = None) -> str|None:
    '''fetches environment variables. used in lifespan events on app startup.'''
    if config_path is None: toolsui_toml_filepath = app_path + "/configs/toolsui.toml"
    else: toolsui_toml_filepath = config_path

    path_success = os.path.isfile(toolsui_toml_filepath)
    if not path_success: return f"Config File does not exist: {toolsui_toml_filepath}"
    try:
        with open(toolsui_toml_filepath, "rb") as f:
            data = tomllib.load(f)
    except TOMLDecodeError as Err: return f"Error importing config file: {toolsui_toml_filepath}\n   {Err}"
    else:
        for item in data.keys():
            os.environ[item] = data[item]
    return None

@asynccontextmanager
async def lifespan(app: FastAPI):
    err_msg = await get_env()
    if err_msg is None: yield
    else: print(err_msg); yield

toolsui = FastAPI(
    title="ToolsUI",
    description="API used to test various front end frameworks with HTMX.",
    version="1.0.0",
    contact={
        "name": "Rashin",
        "email":"jerry@bytesoffury.com",
        "url":"https://github.com/Rash-in/toolsui"
    },
    license_info={
        "name":"Apache License 2.0",
        "identifier": "Apache-2.0"
    },
    swagger_ui_parameters={
        "syntaxHighlight.theme": "obsidian",
        "docExpansion":"none"
    },
    lifespan=lifespan
)

@toolsui.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers['X-Process-Time'] = str(process_time)
    return response


toolsui.mount("/static", StaticFiles(directory=app_path + "/static"), name="static")
toolsui.include_router(default_routers, tags=['default'])

def main():
    hypercorn_config = config.from_toml(hypercorn_config_path)
    asyncio.run(serve(toolsui, hypercorn_config))
if __name__ == "__main__":
    main()