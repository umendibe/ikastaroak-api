from fastapi import APIRouter

ikasleak_router = APIRouter(
    prefix="/ikasleak",
    tags=["Ikasleak"]
)


# 3. Ariketa
@ikasleak_router.get("/ikasle")
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


# 2. Ariketa
@ikasleak_router.get("/{ikasle_id}")
def get_ikasle(ikasle_id: int):
    return {"ikasle_id": ikasle_id}