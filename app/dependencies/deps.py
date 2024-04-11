import re

from fastapi import HTTPException, Depends

from app.models.model import SimpleModel, ExpressionModel
from app.settings.constants import EXPRESSION_PATTERN, BASE_OPERATORS


async def get_expression(
    expression: ExpressionModel = Depends(),
) -> SimpleModel:
    """Function takes an input math expression and returns a SimpleModel object representing the expression"""
    match = re.match(EXPRESSION_PATTERN, expression.source)
    if match:
        input_value = {
            "expression": expression.source,
            'number_one': match.group(1),
            'operator': BASE_OPERATORS[match.group(3)],
            'number_two': match.group(4)
        }
        return SimpleModel(**input_value)
    else:
        raise HTTPException(status_code=404)
