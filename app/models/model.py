from fastapi import HTTPException
from pydantic import BaseModel, Field, computed_field

from app.settings import constants
from app.models.operators import SimpleNumber


class ExpressionModel(BaseModel):
    """The model to check an input math expression"""

    source: str = Field(pattern=constants.EXPRESSION_PATTERN)


class SimpleModel(BaseModel):
    """The model represents a simple mathematical expression."""

    expression: str
    number_one: int
    number_two: int
    operator: str

    @computed_field
    @property
    def result(self) -> int:
        number = SimpleNumber(self.number_one)
        method = getattr(number, self.operator)
        if not method:
            raise HTTPException(status_code=404)
        return method(self.number_two)
