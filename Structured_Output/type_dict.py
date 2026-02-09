from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str

person = Person(name="Aman",age=30,email="amasingrawat@gmail.com")

print(person)