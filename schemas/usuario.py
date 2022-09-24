from typing import Optional
from pydantic import BaseModel

class Usuario(BaseModel):
        id_usuario : Optional[str]
        nombre_usuario :str
        passw : str
        jugador: int
        nivel:int