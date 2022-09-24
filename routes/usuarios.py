from fastapi import APIRouter, Response, status
from config.db import conn
from cryptography.fernet import Fernet
from models.usuarios import usuarios
from schemas.usuario import Usuario
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()
f = Fernet(key)
usuario = APIRouter()


@usuario.get("/usuario", response_model=list[Usuario], tags=["usuarios"])
def get_usuarios():
    return conn.execute(usuarios.select()).fetchall()


@usuario.post("/usuario", response_model=Usuario, tags=["usuarios"])
def create_usuario(usuario: Usuario):
    nuevo_usuario = {"nombre_usuario": usuario.nombre_usuario,
                    "passw": f.encrypt(usuario.passw.encode("utf-8")),
                    "jugador": usuario.jugador,
                    "nivel": usuario.nivel}
    result = conn.execute(usuarios.insert().values(nuevo_usuario))

    return conn.execute(usuarios.select().where(usuarios.c.id_usuario == result.lastrowid)).first()


@usuario.get("/usuario/{id}", response_model=Usuario, tags=["usuarios"])
def get_usuario(id: str):
    return conn.execute(usuarios.select().where(usuarios.c.id_usuario == id)).first()


@usuario.delete("/usuario/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["usuarios"])
def delete_usuario(id: str):
    conn.execute(usuarios.delete().where(usuarios.c.id_usuario == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@usuario.put("/usuario/{id}", response_model=Usuario, tags=["usuarios"])
def update_usuario(id: str, usuario: Usuario):
    conn.execute(usuarios.update().values(nombre_usuario=usuario.nombre_usuario,
    passw=f.encrypt(usuario.passw.encode("utf-8"))).where(usuarios.c.id_usuario == id),
    jugador = usuario.jugador,
    nivel = usuario.nivel)
    return conn.execute(usuarios.select().where(usuarios.c.id_usuario == id)).first()
