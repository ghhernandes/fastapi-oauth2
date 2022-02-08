from fastapi import FastAPI

from .routes import users, token

app = FastAPI()
app.include_router(users.router)
app.include_router(token.router)

@app.get("/")
async def root():
    return {"message": "OAuth2 implementation with FastAPI"}




