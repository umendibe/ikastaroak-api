from fastapi import FastAPI
from routers import ikastaroak

app = FastAPI()

# Router-a aplikazio nagusira gehitu
app.include_router(ikastaroak.router)


# 1. Ariketa
@app.get("/")
def ongietorria():
    return {"izena": "Urko", "ikas_izena": "2DAW"}


# 2. Ariketa
@app.get("/ikasleak/{ikasle_id}")
def get_ikasle(ikasle_id: int):
    return {"ikasle_id": ikasle_id}


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