from pydantic import BaseModel, field_validator, EmailStr
import re

class PersonBase(BaseModel):
    name : str
    email : EmailStr

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if len(value) > 20:
            raise ValueError("Name must be less than 20 characters")
        pattern = r'^[a-zA-Z\s]+$'
        if not bool(re.match(pattern, value)):
            raise ValueError("name cannot contain numbers,special characters or symbols")
        return value

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        allowed_domains = ["gmail.com", "yahoo.com", "outlook.com"]  
        domain = value.split("@")[-1]
        if domain not in allowed_domains:
            raise ValueError(f"Email domain must be one of: {', '.join(allowed_domains)}")

        return value

class PersonRequestSchema(PersonBase):
    pass

class PersonResponseSchema(PersonBase):
    id : int

class PersonUpdateSchema(PersonBase):
    pass