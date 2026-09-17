from fastapi import FastAPI
from app.routes.transform import router as transform_router

app = FastAPI(title="Text Transformer API", description="An API for transforming text into different styles.", version="1.0.0")

app.include_router(transform_router, prefix="/api/v1")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)