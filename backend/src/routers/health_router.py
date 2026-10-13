from main import app


@app.get("/health")
async def root():
    return {"message": "Backend is healthy"}