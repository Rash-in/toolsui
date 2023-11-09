import os, asyncio
from hypercorn.asyncio import serve
from hypercorn import Config
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes import default_routers

app_path = os.path.dirname(os.path.abspath(__file__))
hypercorn_config_path = app_path + "/configs/hypercorn.toml"
config = Config()

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
    }

)
toolsui.mount("/static", StaticFiles(directory=app_path + "/static"), name="static")
toolsui.include_router(default_routers, tags=['default'])

def main():
    hypercorn_config = config.from_toml(hypercorn_config_path)
    asyncio.run(serve(toolsui, hypercorn_config))
if __name__ == "__main__":
    main()