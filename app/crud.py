from sqlalchemy.orm import Session
from . import models

def guardar_datos(db: Session, humedad1: float, humedad2: float, humedad3: float):
    nuevo_dato = models.SensorData(
        humedad1=humedad1,
        humedad2=humedad2,
        humedad3=humedad3
    )
    db.add(nuevo_dato)
    db.commit()
    db.refresh(nuevo_dato)
    return nuevo_dato

def obtener_historial(db: Session):
    return db.query(models.SensorData).order_by(models.SensorData.fecha.desc()).all()
