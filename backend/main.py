from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Log


# import fucntions from database
from database import create_log

app = FastAPI() # intitating FastAPI app here.


origins = ["http://localhost:3000"] # the react origin

# Provide Cross Origin Resource Sharing Functionalities

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

# api - endpoints

@app.get('/')
async def root():
    return {
        "my" : "app"
    }



@app.post('/create-log', response_model= Log)
async def create_log_entry(log: Log):
    response = await create_log(log.dict())
    if response:
        return response
    else: 
        raise HTTPException(400, 'Bad Request')


