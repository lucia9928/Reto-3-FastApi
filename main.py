import re
from typing import Optional, List

from fastapi import FastAPI, HTTPException, Path, Query, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, EmailStr, field_validator
app=FastAPI()
# ---------------------------
# Persistencia en memoria
# ---------------------------
usuarios = {}
productos = {}

next_user_id = 1
next_product_id = 1

# ---------------------------
# Modelos Pydantic
# ---------------------------
# Expresión regular para validación de username
USERNAME_RE = re.compile(r"^[A-Za-z0-9_]+$")

class UsuarioIn(BaseModel):
 username: str
 email: str =Field(min_legth=6 , max_legth=120)
 password: str = Field( min_legth=8, max_legth=64)
 edad: int = Field( gt=0, ge=120)
@field_validator("username")
@classmethod
def validar_username(cls, v: str) -> str:
    if not USERNAME_RE.fullmatch(v):
      v=" "
      raise ValueError("username solo puede contener letras, números y '_'")
    return v

@field_validator("password")
@classmethod
def validar_password(cls, v: str) -> str:
    # r"..." indica una raw string (evita tener que escapar barras).
    if not re.search(r"[A-Z]", v):
        return v
# TO DO
# Completar las validaciones de contraseña:
# "Debe contener al menos una mayúscula"
# "Debe contener al menos una minúscula"
# "Debe contener al menos un número"




class UsuarioOut(BaseModel):
  # TODO
  pass


class UsuarioUpdateIn(BaseModel):
  # TODO
  pass


class ProductoIn(BaseModel):
    # TODO
    pass

    @field_validator("tags")
    @classmethod
    def validar_tags(cls, v: List[str]) -> List[str]:
        # TODO.
        # v contiene una lista de tags
        # Completar las validaciones de tags:
        # "Máximo 5 tags"
        # "Cada tag debe tener entre 2 y 20 caracteres"

        return v

class ProductoOut(BaseModel):
    # TODO
    pass


# ---------------------------
# Endpoints Usuarios
# ---------------------------

# TODO: indicar endpoint de creación de usuario aquí
def crear_usuario(usuario: UsuarioIn):
    global next_user_id

    # TODO:
    # Guardar información de usuario en lista de usuarios (con id incremental)
    # Devolver usuario (UsuarioOut)
    pass
    #return user_out


@app.get("/usuarios/{user_id}", response_model=UsuarioOut)
def obtener_usuario(user_id: int = Path(..., ge=1)):
    # TODO:
    pass


@app.put("/usuarios/{user_id}", response_model=UsuarioOut)
def reemplazar_usuario(
    user_id: int = Path(..., ge=1),
    #payload: UsuarioUpdateIn
):
    # TODO:
    pass


# ---------------------------
# Endpoints Productos
# ---------------------------
    # TODO:


# ---------------------------
# Endpoints auxiliares
# ---------------------------

@app.get("/debug/validation-summary")
def validation_summary(
    mode: str = Query("short", pattern="^(short|full)$"),
):
    # TODO:
    pass