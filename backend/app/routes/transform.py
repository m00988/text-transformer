from fastapi import APIRouter, HTTPException
from app.schemas import TransformResponseModel, TransformRequestModel
from app.services.transform import transform_text

router = APIRouter(tags=["Transform"], prefix="/transform")

@router.post("/", response_model=TransformResponseModel)
async def transform(request: TransformRequestModel):

    try:
        return await transform_text(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
