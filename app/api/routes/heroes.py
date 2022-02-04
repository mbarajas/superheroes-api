from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["heroes"])
async def get_heroes():
    return [{"name": "Batman"}, {"name": "Superman"}]
