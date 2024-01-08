# Raising an Exception

```python
class Command(BaseModel):
   name: str
   description: str

    def exec(self):
        raise NotImplementedError('This method was not yet implemented.')
```
