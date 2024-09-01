from fastapi import FastAPI
from auth.schemas import UserRead, UserCreate
from auth.auth import auth_backend, fastapi_users
from notes.router import router as router_notes


app = FastAPI(
    title="Trading App"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    router_notes
)
