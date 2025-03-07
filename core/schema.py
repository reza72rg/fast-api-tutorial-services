from pydantic import BaseModel

class PersonBase(BaseModel):
    name : str

class PersonRequestSchema(PersonBase):
    pass

class PersonResponseSchema(PersonBase):
    id : int

class PersonUpdateSchema(PersonBase):
    pass