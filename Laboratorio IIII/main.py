from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    categoria: str

productos: list[Producto] = [
    Producto(id=1, nombre="Celular", precio=150000.0, categoria="Electronico"),
    Producto(id=2, nombre="Notebook", precio=350000.0, categoria="Electronico"),
    Producto(id=3, nombre="Mouse", precio=5000.0, categoria="Electronico"),
    Producto(id=4, nombre="Silla", precio=5000.0, categoria="Muebles"),
    Producto(id=5, nombre="Mesa", precio=5000.0, categoria="Muebles")
]

@app.get("/productos/", response_model=list[Producto])
def get_productos():
    return productos

@app.get("/productos/{producto_id}", response_model=Producto)
def get_producto(producto_id: int):
    for producto in productos:
        if producto.id == producto_id:
            return producto
    raise HTTPException(status_code=404, detail=f"Producto {producto_id} no encontrado")

@app.post("/productos/", response_model=Producto)
def crear_poducto(producto: Producto):
    for producto_existe in productos:
        if producto_existe.id == producto.id:
            raise HTTPException(status_code=400, detail=f"Producto {producto.id} ya existe")
    productos.append(producto)
    return producto

@app.put("/productos/{producto_id}", response_model=Producto)
def actualizar_producto(id: int, producto_actualizado: Producto):
    for index, producto in enumerate(productos):
        if producto.id == id:
            productos[index] = producto_actualizado
            return producto_actualizado
    raise HTTPException(status_code=404, detail=f"Producto {id} no encontrado")

@app.delete("/productos/{id}", status_code=204)
def eliminar_producto(id: int):
    for index, producto in enumerate(productos):
        if producto.id == id:
            productos.pop(index)
            return
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.get("/productos/categoria/{categoria}", response_model=list[Producto])
def get_productos_por_categoria(categoria: str):
    categoria = categoria.lower()
    productos_filtrados = []
    for producto in productos:
        if producto.categoria.lower() == categoria:
            productos_filtrados.append(producto)
    if not productos_filtrados:
        raise HTTPException(status_code=404, detail=f"No se encontraron productos en la categoría {categoria}")
    return productos_filtrados