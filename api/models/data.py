from pydantic import BaseModel


class Card(BaseModel):
    id: int
    name: str
    content: str
    user: 'User'

    class Config:
        from_attributes = True


class User(BaseModel):
    id: int
    name: str
    hashed_password: str
    progress: int

    cards: list[Card]

    class Config:
        from_attributes = True
