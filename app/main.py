from fastapi import FastAPI
from app.api.places import router as places_router
from app.api.users import router as users_router
from app.api.wishes import router as wishes_router

app = FastAPI()

app.include_router(places_router)
app.include_router(users_router)
app.include_router(wishes_router)