from fastapi import FastAPI
from routers import router

app = FastAPI()
app.include_router(router=router)

@app.get("/")
async def home():
    return {"msg": "Bem-vindo a página Home"} 

