from fastapi import FastAPI

app = FastAPI(

   title="Mi primera API Yordan appyCastro",
    description="Esta es mi primera API creada con FastAPI yo puedo",
    version = "1.0.0",

)

@app.get("/")
async def root():
          """Endpoint raíz que devuelve un mensaje de bienvenida."""
          return {"¡Bienvenido a mi primera API Yordan!"}   

#paso 4 Definirel endpoint con un parametro de ruta
@app.get("/saludo{nombre}")
#funcion que recibe el parametro de ruta y devuelve un mensaje de saludo personalizado
def saludo(nombre: str):
        """Endpoint que saludaa la persona cuyo nombre se proporciona en la ruta."""
        if nombre == "admin":
            return {"mensaje":"Hola, admin! Bienvenido a la API."}
        elif nombre == "Yordan":
            return {"mensaje":"Hola hdp"}
        else:
            return {"mensaje": f"Hola, {nombre}. No tienes acceso a esta API."}
          


