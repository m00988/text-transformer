from pydantic import BaseModel, Field
from enum import Enum


class StyleModel(str, Enum):
    SUMMARY = "Summary"
    FORMAL = "Formal"
    EXPAND_TEXT = "Expand_text"
    INFORMAL = "Informal"
    REVIEW_TEXT = "Review_text"


class TransformBaseModel(BaseModel):
    text: str = Field(..., min_length=50, max_length=1000,
                      description="Enter a text; the text must be longer than 50 characters.")

    style: StyleModel = Field(..., description="Select a style for the transformed text.")

class TransformRequestModel(TransformBaseModel):
    pass

class TransformResponseModel(BaseModel):
    transformed_text: str = Field(..., description="The transformed text based on the selected style.")