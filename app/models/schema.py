from typing import Any

from pydantic import BaseModel


class ResultSchema(BaseModel):
    """
    The model represents the schema for a result,
    which consists of an expression and its corresponding result.
    """

    expression: str
    result: Any

