from fastapi import APIRouter

router = APIRouter(
    prefix="/projects",
    tags=["projects"],
)

@router.get("/")
def app_root():
    return {"message": "Create a new project and get a project token"}