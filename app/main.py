from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/api/health")
def healthcheck():
    return {
        "status": "ok",
        "served_by": socket.gethostname()
    }