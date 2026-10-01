from fastapi import FastAPI

from routers import ikasleak, ikastaroak

app = FastAPI()

# Router-a aplikazio nagusira gehitu (ikastaroak.py-ko endpoint guztiak)
app.include_router(ikastaroak.router)
app.include_router(ikasleak.ikasleak_router)


# 1. Ariketa
@app.get("/")
def ongietorria():
    return {"izena": "Urko", "ikas_izena": "2DAW"}