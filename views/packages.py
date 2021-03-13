from fastapi import APIRouter

router = APIRouter()


@router.get("/packages")
def packages():
    return {}