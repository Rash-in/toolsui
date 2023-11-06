import os, asyncio
from hypercorn.asyncio import serve
from hypercorn import Config
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes import default_routers

app_path = os.path.dirname(os.path.abspath(__file__))
hypercorn_config_path = app_path + "/configs/hypercorn.toml"
config = Config()

toolsui = FastAPI()
toolsui.mount("/static", StaticFiles(directory=app_path + "/static"), name="static")
toolsui.include_router(default_routers, tags=['default'])

def main():
    hypercorn_config = config.from_toml(hypercorn_config_path)
    asyncio.run(serve(toolsui, hypercorn_config))
if __name__ == "__main__":
    main()