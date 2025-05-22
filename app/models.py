from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.sql import func
from .database import Base

class SensorData(Base):
    __tablename__ = "sensor_data"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    humedad1 = Column(Float)
    humedad2 = Column(Float)
    humedad3 = Column(Float)
    fecha = Column(DateTime, default=func.now())
