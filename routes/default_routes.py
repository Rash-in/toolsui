import os
from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

routes_path = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.dirname(routes_path)

favicon_path = app_path + "/static/favicon.ico"
healthcheck_path = app_path + "/static/healthcheck.html"

@router.get("/favicon.ico", include_in_schema=False)
def get_favicon():
    return FileResponse(favicon_path)

@router.get("/healthcheck", include_in_schema=False)
def get_healthcheck():
    return FileResponse(healthcheck_path)