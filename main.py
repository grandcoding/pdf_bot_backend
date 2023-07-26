from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routers import api

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def index():
    return {
        'msg': 'API TEST'
    }

app.include_router(
  api.router,
  prefix="/bot"
)
