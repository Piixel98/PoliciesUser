from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER

from core.config import config
from core.exceptions import CustomException
from core.fastapi.middlewares import (
    AuthenticationMiddleware,
    AuthBackend,
)
from core.fastapi.dependencies import Logging
from api import router


def init_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.CORS_ORIGINS,
        allow_credentials=config.CORS_ALLOW_CREDENTIALS,
        allow_methods=config.CORS_METHODS,
        allow_headers=config.CORS_HEADERS,
    )


def init_routers(app: FastAPI) -> None:
    app.include_router(router)


def init_listeners(app: FastAPI) -> None:
    # Exception handler
    @app.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"code": exc.code, "error_code": exc.error_code, "message": exc.message},
        )


def on_auth_error(request: Request, exc: Exception):
    status_code, error_code, message = 401, None, str(exc)
    if isinstance(exc, CustomException):
        status_code = int(exc.code)
        error_code = exc.error_code
        message = exc.message

    return JSONResponse(
        status_code=status_code,
        content={"error_code": error_code, "message": message},
    )


def init_middleware(app: FastAPI) -> None:
    app.add_middleware(
        AuthenticationMiddleware,
        backend=AuthBackend(),
        on_error=on_auth_error,
    )


def add_redirect_main_page(app: FastAPI) -> None:
    @app.get("/", include_in_schema=False)
    async def root():
        return RedirectResponse(url=f"/docs/", status_code=HTTP_303_SEE_OTHER)


def create_app() -> FastAPI:
    app = FastAPI(
        title="API PoliciesUser",
        version="1.0.0",
        docs_url=None if config.ENV == "pro" else "/docs",
        redoc_url=None if config.ENV == "pro" else "/redoc",
        dependencies=[Depends(Logging)],
    )
    init_routers(app=app)
    init_cors(app=app)
    init_listeners(app=app)
    init_middleware(app=app)
    add_redirect_main_page(app=app)
    return app


app = create_app()
