from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.settings import settings
from app.routers.travel import router as travel_router

from app.routers.guide import router as guide_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(travel_router)

app.include_router(guide_router)


@app.get("/")
def root():
    return {
        "message": "AI Travel Companion API",
        "version": settings.VERSION,
    }