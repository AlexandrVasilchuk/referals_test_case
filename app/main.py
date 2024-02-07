from fastapi import FastAPI

from app.api.endpoints import referral_router, user_router

app = FastAPI()
app.include_router(user_router)
app.include_router(referral_router)
