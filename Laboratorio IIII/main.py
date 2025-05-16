from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr, field_validator
from datetime import datetime
from enum import Enum
from typing import List

app = FastAPI()

class Categoria(BaseModel):
    id_categoria: int = Field(gt=0)
    descripcion: str


class Producto(BaseModel):
    id: int = Field(gt=0)
    nombre: str
    precio: float
    categoria: Categoria

class Usuario(BaseModel):
    id: int = Field(gt=0)
    apellido: str
    nombre: str
    correo: EmailStr
    password: str = Field(min_length=8)
    pais: str
    ciudad: str
    direccion: str
    telefono: str
    rol: str = Field(default= "Cliente")

    @field_validator("password")
    def tiene_mayuscula(cls, v:str) -> str:
        if not any(caracter.isupper() for caracter in v):
            raise ValueError("La contraseña debe contener almenos 1 mayuscula")
        return v    

    @field_validator("rol")
    def rol_correcto(cls, v: str) -> str:
        roles_permitidos = ["Cliente", "Administrador"]
        if v not in roles_permitidos:
            raise ValueError(f"Coloque un rol válido: {roles_permitidos}")
        return v


class EstadoDespoacho(str, Enum):
    despachado = "Despachado"
    no_despachado = "No despachado"

class Venta(BaseModel):
    id: int = Field(gt=0)
    idUsuario: Usuario
    idProducto: Producto
    cantidad: int
    fecha: datetime
    despachado: EstadoDespoacho


ventasDict = [
    {
        "id": 1,
        "idUsuario": {
            "id": 1,
            "apellido": "Perez",
            "nombre": "Juan",
            "correo": "5mLJt@gmail.com",
            "password": "A12345678",
            "pais": "Argentina",
            "ciudad": "Cordoba",
            "direccion": "Calle 1",
            "telefono": "123456789",
            "rol": "Cliente"
        },
        "idProducto": {
            "id": 1,
            "nombre": "Celular",
            "precio": 150000,
            "categoria": {
                "id_categoria": 1,
                "descripcion": "Electrónica"
            }
        },
        "cantidad": 0,
        "fecha": "2025-04-26T19:53:33.847000Z",
        "despachado": "Despachado" 
    }
]



usuariosDict = [
    {
        "id": 1,
        "apellido": "Perez",
        "nombre": "Juan",
        "correo": "5mLJt@gmail.com",
        "password": "A12345678",
        "pais": "Argentina",
        "ciudad": "Cordoba",
        "direccion": "Calle 1",
        "telefono": "123456789",
        "rol": "Cliente"
    },
    {
        "id": 2,
        "apellido": "Gomez",
        "nombre": "Pedro",
        "correo": "K5Ct0@gmail.com",
        "password": "B12345678",
        "pais": "Argentina",
        "ciudad": "Villa Maria",
        "direccion": "Calle 2",
        "telefono": "123456789",
        "rol": "Administrador"
    }
]

categoriasDict = [
    {
        "id_categoria": 1,
        "descripcion": "Electrónica"
    },
    {
        "id_categoria": 2,
        "descripcion": "Muebles"
    }
]


productosDict = [
    {
        "id": 1,
        "nombre": "Celular",
        "precio": 150000.0,
        "categoria": {
            "id_categoria": 1,
            "descripcion": "Electrónica"
        }
    },
    {
        "id": 2,
        "nombre": "Notebook",
        "precio": 350000.0,
        "categoria": {
            "id_categoria": 1,
            "descripcion": "Electrónica"
        }
    },
    {
        "id": 3,
        "nombre": "Mouse",
        "precio": 5000.0,
        "categoria": {
            "id_categoria": 1,
            "descripcion": "Electrónica"
        }
    },
    {
        "id": 4,
        "nombre": "Silla",
        "precio": 5000.0,
        "categoria": {
            "id_categoria": 2,
            "descripcion": "Muebles"
        }
    },
    {
        "id": 5,
        "nombre": "Mesa",
        "precio": 5000.0,
        "categoria": {
            "id_categoria": 2,
            "descripcion": "Muebles"
        }
    }
]

ventas: List[Venta] = [Venta(**v) for v in ventasDict]
usuarios: List[Usuario] = [Usuario(**v) for v in usuariosDict]
categorias: List[Categoria] = [Categoria(**v) for v in categoriasDict]
productos: List[Producto] = [Producto(**v) for v in productosDict]


def validar_categoria(id_categoria: int) -> Categoria:
    for categoria in categorias:
        if categoria.id_categoria == id_categoria:
            return categoria
    return None

def validar_producto(id_producto: int) -> Producto:
    for producto in productos:
        if producto.id == id_producto:
            return producto
    return None

def validar_usuario(id_usuario: int) -> Usuario:
    for usuario in usuarios:
        if usuario.id == id_usuario:
            return usuario
    return None


# Endpoints de productos
@app.get("/productos/", response_model=list[Producto], tags=["Productos"])
def get_productos():
    return productos


@app.get("/productos/{producto_id}", response_model=Producto, tags=["Productos"])
def get_producto(producto_id: int):
    for producto in productos:
        if producto.id == producto_id:
            return producto
    raise HTTPException(status_code=404, detail=f"Producto {producto_id} no encontrado")


@app.post("/productos/", response_model=Producto, tags=["Productos"])
def crear_producto(producto: Producto):
    categoria = validar_categoria(producto.categoria.id_categoria)
    if not categoria:
        raise HTTPException(status_code=400, detail="La categoría no es válida")
    for producto_existe in productos:
        if producto_existe.id == producto.id:
            raise HTTPException(status_code=400, detail=f"Producto {producto.id} ya existe")
    producto.categoria = categoria
    productos.append(producto)
    return producto


@app.put("/productos/{producto_id}", response_model=Producto, tags=["Productos"])
def actualizar_producto(producto_id: int, producto_actualizado: Producto):
    categoria = validar_categoria(producto_actualizado.categoria.id_categoria)
    if not categoria:
        raise HTTPException(status_code=400, detail="La categoría no es válida")
    for index, producto in enumerate(productos):
        if producto.id == producto_id:
            producto.nombre = producto_actualizado.nombre
            producto.precio = producto_actualizado.precio
            producto.categoria = categoria
            return producto
    raise HTTPException(status_code=404, detail=f"Producto {producto_id} no encontrado")

@app.delete("/productos/{id}", tags=["Productos"])
def eliminar_producto(id: int):
    for index, producto in enumerate(productos):
        if producto.id == id:
            productos.pop(index)
            return
    raise HTTPException(status_code=404, detail="Producto no encontrado")


@app.get("/productos/categoria/{categoria}", response_model=list[Producto], tags=["Productos"])
def get_productos_por_categoria(categoria: int):
    productos_filtrados = [producto for producto in productos if producto.categoria.id_categoria == categoria]
    if not productos_filtrados:
        raise HTTPException(status_code=404, detail=f"No se encontraron productos en la categoría {categoria}")
    return productos_filtrados


# Endpoints de usuarios
@app.get("/usuarios/", response_model=list[Usuario], tags=["Usuarios"])
def get_usuarios():
    return usuarios


@app.post("/usuarios/", response_model=Usuario, tags=["Usuarios"])
def crear_usuario(usuario: Usuario):
    for user in usuarios:
        if user.id == usuario.id:
            raise HTTPException(status_code=400, detail=f"Usuario {usuario.id} ya existe")
    usuarios.append(usuario)
    return usuario

@app.put("/usuarios/{id_usuario}", response_model=Usuario, tags=["Usuarios"])
def actualizar_usuario(id_usuario: int, usuario_actualizado: Usuario):
    for index, usuario in enumerate(usuarios):
        if usuario.id == id_usuario:
            usuario_actualizado.id = id_usuario
            usuarios[index] = usuario_actualizado
            return usuario_actualizado
    raise HTTPException(status_code=404, detail=f"Usuario {id_usuario} no encontrado")


@app.delete("/usuarios/{id}", tags=["Usuarios"])
def eliminar_usuario(id: int):    
    for index, usuario in enumerate(usuarios):
        if usuario.id == id:
            usuarios.pop(index)
            return
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


# Endpoints de categorias
@app.get("/categoria/", response_model=list[Categoria], tags=["Categorias"])
def get_categorias():
    return categorias

@app.post("/categorias/", response_model=Categoria, tags=["Categorias"])
def crear_categoria(categoria: Categoria):
    for categoria_existe in categorias:
        if categoria_existe.id_categoria == categoria.id_categoria:
            raise HTTPException(status_code=400, detail=f"Categoria {categoria.id_categoria} ya existe")
    categorias.append(categoria)
    return categoria


@app.put("/categorias/{id_categoria}", response_model=Categoria, tags=["Categorias"])
def actualizar_categoria(id_categoria: int, categoria_actualizada: Categoria):
    for index, categoria in enumerate(categorias):
        if categoria.id_categoria == id_categoria:
            categoria_actualizada.id_categoria = id_categoria
            categorias[index] = categoria_actualizada
            return categoria_actualizada
    raise HTTPException(status_code=404, detail=f"Categoria {id_categoria} no encontrada")


@app.delete("/categorias/{id_categoria}", tags=["Categorias"])
def eliminar_categoria(id_categoria: int):
    for index, categoria in enumerate(categorias):
        if categoria.id_categoria == id_categoria:
            categorias.pop(index)
            return
    raise HTTPException(status_code=404, detail="Categoria no encontrada")

# Endpoints de ventas
@app.get("/ventas/", response_model=list[Venta], tags=["Ventas"])
def get_ventas():
    return ventas

@app.post("/ventas/", response_model=Venta, tags=["Ventas"])
def crear_venta(venta: Venta):
    producto = validar_producto(venta.idProducto.id)
    usuario = validar_usuario(venta.idUsuario.id)
    if not producto:
        raise HTTPException(status_code=400, detail=f"Producto {venta.idProducto.id} no existe")
    if not usuario:
        raise HTTPException(status_code=400, detail=f"Usuario {venta.idUsuario.id} no existe")
    for venta_existe in ventas:
        if venta_existe.id == venta.id:
            raise HTTPException(status_code=400, detail=f"Venta {venta.id} ya existe")
    venta.idProducto = producto
    venta.idUsuario = usuario  
    ventas.append(venta)
    return venta

@app.put("/venta/{id_venta}", response_model=Venta, tags=["Ventas"])
def actualizar_despacho(id_venta: int, despacho_actualizado: EstadoDespoacho):
    for venta in ventas:
        if venta.id == id_venta:
            venta.despachado = despacho_actualizado
            return venta
    raise HTTPException(status_code=404, detail=f"Venta {id_venta} no encontrada")