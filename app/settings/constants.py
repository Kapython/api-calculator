EXPRESSION_PATTERN = r'^(\d+(\.\d+)?)\s*([-+*/])\s*(\d+(\.\d+)?)$'
BASE_OPERATORS = {
        "+": "__add__",
        "-": "__sub__",
        "/": "__truediv__",
        "*": "__mul__"
    }

