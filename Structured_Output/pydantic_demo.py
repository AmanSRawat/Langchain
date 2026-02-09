from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str = 'Aman'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=10)

student_name = {'age':22,'email':'abc@gmail.com','cgpa':8.5}
student = Student(**student_name)

print(student)