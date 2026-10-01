from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(
    prefix="/ikastaroak",
    tags=["Ikastaroak"]
)

ikastaroak_db = [
    {"id": 1, "izena": "ikastaro1", "prezioa": 50, "maila": "hasiberria"},
    {"id": 2, "izena": "ikastaro2", "prezioa": 100, "maila": "hasiberria"},
    {"id": 3, "izena": "ikastaro3", "prezioa": 150, "maila": "aurreratua"},
]

class IkastaroaSarrera(BaseModel):
    izena: str
    prezioa: float
    maila: str


# 4. Ariketa: Guztiak lortu edo mailaren arabera filtratu
@router.get("")
def get_ikastaroak(maila: str | None = None):
    if not maila:
        return ikastaroak_db

    ikastaroak_db_filtratu = []
    for ikastaro in ikastaroak_db:
        if ikastaro["maila"] == maila:
            ikastaroak_db_filtratu.append(ikastaro)
            
    return ikastaroak_db_filtratu


# 4. Ariketa: ID bidez lortu
@router.get("/{id}")
def get_ikastaroak_id(id: int):
    for ikastaro in ikastaroak_db:
        if ikastaro["id"] == id:
            return ikastaro
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Ez da aurkitu ID hori"
    )


# 5. Ariketa: Ikastaro berria sortu
@router.post("", status_code=status.HTTP_201_CREATED)
def post_ikastaroak(ikastaro_berria: IkastaroaSarrera):
    id_berria = ikastaroak_db[-1]["id"] + 1 if ikastaroak_db else 1

    ikastaroak_dict = ikastaro_berria.model_dump()
    ikastaroak_dict["id"] = id_berria

    ikastaroak_db.append(ikastaroak_dict)

    return ikastaroak_dict