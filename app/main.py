from fastapi import FastAPI
from app.places.places_router import router as places_router
from app.users.users_router import router as users_router
from app.users.admin_router import router as admin_router
from app.authentication.auth_router import router as auth_router

app = FastAPI()

app.include_router(places_router)
app.include_router(users_router)
app.include_router(admin_router)
app.include_router(auth_router)