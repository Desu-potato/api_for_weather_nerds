from fastapi import Depends, FastAPI, status
from .models import tablemodels, schemas
from .database import engine
from .routers import create, auth


API_NAME = "Nerdy"



app = FastAPI()
app.include_router(create.router)
app.include_router(auth.router)

tablemodels.Base.metadata.create_all(bind=engine)

@app.get("/", response_model=schemas.Health, status_code=status.HTTP_200_OK )
async def health():
    response = schemas.Health(apiName=API_NAME)
    return response