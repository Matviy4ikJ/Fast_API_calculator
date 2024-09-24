from fastapi import FastAPI, Query, HTTPException
from typing import Union

app = FastAPI()


@app.get('/calculator')
def calculator(num1: Union[int, float] = Query(default=2,description='Enter first number'),
               num2: int | float = Query(default=1, description='Enter second number'),
               operator: str = Query(default=1, description='Enter a operator for first and second number',
                                     enum=['+', '-', '/', '*'])):

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise HTTPException(status_code=400, detail='Division by zero is not allowed')
        result = num1 / num2
    else:
        raise HTTPException(status_code=400, detail='Invalid operator')

    return {
        'expression': f'{num1} {operator} {num2}',
        'result': result
    }
