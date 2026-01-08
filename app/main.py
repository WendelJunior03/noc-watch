from fastapi import FastAPI

app = FastAPI(title="NOC Watch")

@app.get("/")
def root():
    return {"message": "Welcome to NOC Watch"}

@app.get("/health")
def health():
    return {"status": "ok"}