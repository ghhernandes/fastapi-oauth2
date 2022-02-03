from fastapi import FastAPI

from .routes import projects

app = FastAPI()
app.include_router(projects.router)

@app.get("/")
async def root():
    return {"message": "OAuth2 implementation with FastAPI"}




