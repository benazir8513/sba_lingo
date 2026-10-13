from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers.vocab_router import vocab_router

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.include_router(vocab_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def main() -> None:
    print("Hello from backend!")
