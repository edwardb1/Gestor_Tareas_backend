from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.gestor_tareas import models, schemas
from src.gestor_tareas.database import sessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gestor de tareas", version="0.1.0")


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")

def read_root():
    return {"mensaje":"Hola, papu entrenando para rendir como un senior"}

@app.post("/empleos/", response_model=schemas.OfertaLaboral)
def Crear_Oferta(oferta: schemas.OfertaLaboral,db: Session=Depends(get_db)):
    nueva_oferta = models.OfectaLaboralDB(
        titulo=oferta.titulo,
        empresa=oferta.empresa,
        url=str(oferta.url),
        salario=oferta.salario,
        ubicacion=oferta.ubicacion,
        fecha_publicacion=oferta.fecha_publicacion,
        estado=oferta.estado
    )
    db.add(nueva_oferta)
    db.commit()
    db.refresh(nueva_oferta)

    print("guradando oferta para: ",{oferta.empresa})

    return nueva_oferta