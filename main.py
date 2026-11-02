from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
import database
from auth import router as auth_router


models.base.metadata.create_all(bind=database.engine)
app=FastAPI(title="Blogging Site API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Blogging Site API!"}