from routes.user import user
from routes.usuarios import usuario
from fastapi import FastAPI


app = FastAPI()


app.include_router(user)
app.include_router(usuario)

