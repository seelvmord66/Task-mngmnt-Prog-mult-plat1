from fastapi import FastAPI, HTTPException
import controllers.task_controller
from fastapi.openapi.models import Info
from fastapi.openapi.models import Contact
from fastapi.openapi.models import License
from fastapi.openapi.models import Info, Contact, License
from starlette.responses import RedirectResponse, JSONResponse
from fastapi.openapi.docs import get_swagger_ui_html

import uvicorn
from fastapi import APIRouter
from .services.task_service import TaskService
from .models.task_model import Task, TaskCreate, TaskUpdate

app = FastAPI()

app_metadata = Info(
    title="Task Management com fastAPI",
    version="1.0.0",
    description="API para managing tasks",
    contact=Contact(
        name="Victor Augusto Pires e Silva",
        RA="2041382211047",
        email="victor.silva250@fatec.sp.gov.br"
    ),
    license=License(
        name="MIT License",
        url="https://opensource.org/licenses/MIT"
    )
)



router = APIRouter()
task_service = TaskService()
app.include_router(controllers.task_controller.router)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": str(exc.detail)}
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred"}
    )


@app.get("/", tags=["Redirect"], include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")


@app.get("/docs", tags=["Redirect"], include_in_schema=False)
async def get_swagger_ui():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Swagger UI"
    )




@app.get("/openapi.json", tags=["metadata"])
async def get_openapi_metadata():
    return app.openapi(openapi_version="3.0.2", title="metadata")
                       
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

