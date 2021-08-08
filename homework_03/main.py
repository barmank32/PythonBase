from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Welcome"}


@app.get("/ping/")
async def get_status():
    """Get status of messaging server."""
    return {"status": "pong"}
