from fastapi import FastAPI

from app.api.router import api_router 
app = FastAPI(
    title = "AI DE COPILOT PLATFORM",
    description= "Production grade data engineering platform",
    version="1.0.0.0"
)

app.include_router(api_router)

