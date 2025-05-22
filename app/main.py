from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from . import crud, schemas
from .database import SessionLocal

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db: Session = Depends(get_db)):
    datos = crud.obtener_historial(db)
    return templates.TemplateResponse("index.html", {"request": request, "datos": datos})

@app.post("/guardar_datos/")
async def guardar_datos(datos: schemas.HumedadTripleInput, db: Session = Depends(get_db)):
    nuevo_dato = crud.guardar_datos(db, humedad1=datos.humedad1, humedad2=datos.humedad2, humedad3=datos.humedad3)
    return {"mensaje": "Datos guardados correctamente", "id": nuevo_dato.id}

@app.get("/historial/")
async def obtener_historial(db: Session = Depends(get_db)):
    datos = crud.obtener_historial(db)
    return [
        {
            "id": d.id,
            "fecha": d.fecha.strftime("%Y-%m-%d %H:%M:%S"),
            "humedad1": d.humedad1,
            "humedad2": d.humedad2,
            "humedad3": d.humedad3
        }
        for d in datos
    ]

@app.get("/grafica", response_class=HTMLResponse)
async def ver_grafica(request: Request):
    return templates.TemplateResponse("graficas.html", {"request": request})
