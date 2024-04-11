from http.client import HTTPException

from fastapi import APIRouter, Depends

from app.dependencies import deps
from app.models.model import SimpleModel
from app.models.schema import ResultSchema

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "I'm healthy"}


@router.get("/calc", status_code=200, response_model=ResultSchema)
async def calculate(
    *,
    expression: SimpleModel = Depends(deps.get_expression)
) -> SimpleModel:
    """GET request and returns the result of a mathematical expression"""
    return expression
