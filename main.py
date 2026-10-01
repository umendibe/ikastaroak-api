from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

app = FastAPI()


# 1. Ariketa
@app.get("/")
def ongietorria():
    return {"izena": "Urko", "ikas_izena": "2DAW"}


# 2. Ariketa
@app.get("/ikasleak/{ikasle_id}")
def get_ikasle(id: int):
    return {"ikasle_id": id}


# 3. Ariketa
@app.get("/ikasle")
def get_ikasle2(maila: str | None = None):
    ikasleak_db = [
        {"id": 1, "izena": "Ane", "maila": "DAW2"},
        {"id": 2, "izena": "Jon", "maila": "DAW1"},
        {"id": 3, "izena": "Maider", "maila": "DAW2"},
    ]

    if not maila:
        return ikasleak_db

    ikasle_maila = []
    for ikasle in ikasleak_db:
        if ikasle["maila"] == maila.upper():
            ikasle_maila.append(ikasle)

    return ikasle_maila


# 4. Ariketa
ikastaroak_db = [
    {"id": 1, "izena": "ikastaro1", "prezioa": 50, "maila": "hasiberria"},
    {"id": 2, "izena": "ikastaro2", "prezioa": 100, "maila": "hasiberria"},
    {"id": 3, "izena": "ikastaro3", "prezioa": 150, "maila": "aurreratua"},
]


@app.get("/ikastaroak")
def get_ikastaroak(maila: str | None = None):
    if not maila:
        return ikastaroak_db

    ikastaroak_db_filtratu = []

    for ikastaro in ikastaroak_db:
        if ikastaro["maila"] == maila:
            ikastaroak_db_filtratu.append(ikastaro)
            
    return ikastaroak_db_filtratu


@app.get("/ikastaroak/{id}")
def get_ikastaroak_id(id: int):
    for ikastaro in ikastaroak_db:
        if ikastaro["id"] == id:
            return ikastaro
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Ez da aurkitu ID hori"
    )


# 5. Ariketa
class IkastaroaSarrera(BaseModel):
    izena: str
    prezioa: float
    maila: str


@app.post("/ikastaroak", status_code=status.HTTP_201_CREATED)
def post_ikastaroak(ikastaro_berria: IkastaroaSarrera):
    id_berria = ikastaroak_db[-1]["id"] + 1 if ikastaroak_db else 1

    ikastaroak_dict = ikastaro_berria.model_dump()
    ikastaroak_dict["id"] = id_berria

    ikastaroak_db.append(ikastaroak_dict)

    return ikastaroak_dict