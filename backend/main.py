from fastapi import FastAPI
from routers.vocab_router import vocab_router

app = FastAPI()
app.include_router(vocab_router)

def main() -> None:
    print("Hello from backend!")
