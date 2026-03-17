from fastapi import FastAPI
from routers import user_router, item_router

app = FastAPI()

app.include_router(user_router.router)
app.include_router(item_router.router)