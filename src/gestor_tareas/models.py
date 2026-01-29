from sqlalchemy import Column, Integer, String, Date
from src.gestor_tareas.database import Base

class OfectaLaboralDB(Base):
    """
    Docstring for OfectaLaboralDB
    Este modelo  define la tabla 'ofertas' en la base de datos

    """
    __tablename__="ofertas"
    id= Column(Integer, primary_key=True, index=True)

    titulo=Column(String, index=True)
    empresa=Column(String, index=True)
    url=Column(String, unique=True)
    salario= Column(String, nullable=True)
    ubicacion= Column(String)
    fecha_publicacion= Column(Date)
    estado= Column(String, default="Nuevo")