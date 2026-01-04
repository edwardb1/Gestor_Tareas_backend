from typing import Optional, List
from pydantic import BaseModel, HttpUrl 
from datetime import date

class OfertaLaboral(BaseModel):
    titulo: str
    empresa: str
    url: HttpUrl
    salario: Optional[str]=None
    Ubicacion: str
    fecha_publicacion: date
    Estado: str="nuevo"
    Requisitos: List[str]
    Beneficios: List[str]

class config():
    Json_scheme_example = {
        "example":{
            "titulo":"python developer",
            "empresa": "tech lamb uncle",
            "URL":"https:ksainfans",
            "salario":"3422",
            "Ubicacion": "lugar",
            "Fecha_publicacion": "2026-01-03",
            "estado":"nuevo",#no es necesario incluirlo debido a que esta ya esta rellenada por defecto como nuevo
            "requisitos": ["que se llame pepe", "python"],
            "Beneficios": ["salud", "ingreso a becas"]
        }
    }
