from pydantic import BaseModel

class HumedadTripleInput(BaseModel):
    humedad1: float
    humedad2: float
    humedad3: float

class HumedadTripleResponse(BaseModel):
    mensaje: str
    id: int
