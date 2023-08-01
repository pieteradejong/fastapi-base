from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Application root."}

@router.get("/status")
def read_status():
    return {"message": "Application status."}
