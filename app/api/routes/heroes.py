from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["heroes"])
async def get_heroes():
    return [{"name": "Batman"}, {"name": "Superman"}]

@router.get("/{hero}", tags=["heroes"])
async def get_hero(hero: str):
    return {"name": hero}
