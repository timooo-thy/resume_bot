from fastapi import FastAPI, Request
from time import time
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .services.httpx_service import HTTPXService
import httpx
from .routers import graph_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with httpx.AsyncClient() as client:
        app.state.httpx_client = client
        yield


app = FastAPI(lifespan=lifespan)
app.include_router(graph_router)

origins = [
    "http://localhost:3000",
    "https://www.timooothy.me",
    "https://timooothy.me",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_httpx_service(request: Request) -> HTTPXService:
    client = request.app.state.httpx_client
    return HTTPXService(client)


@app.get("/")
async def main() -> dict[str, str]:
    """
    Root endpoint that returns a welcome message.

    Returns:
        dict: A dictionary containing a welcome message.
    """
    return {"message": "Welcome to the Resume Bot API"}


@app.get("/health")
async def health_check() -> dict[str, str | float]:
    """
    Health check endpoint that returns the status and current timestamp.

    Returns:
        dict: A dictionary containing the status and current timestamp.
    """
    return {"status": "healthy", "timestamp": time(), "version": "1.0.0"}
