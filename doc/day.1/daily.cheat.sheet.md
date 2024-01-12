# Daily Cheat Sheet

## Funkcia

```python
def hello():
   print('Hello world!')
```

## Dátová trieda pomocou modulu `pydantic`

```python
from pydantic import BaseModel


class User(BaseModel):
   id: int
   name: str
```
